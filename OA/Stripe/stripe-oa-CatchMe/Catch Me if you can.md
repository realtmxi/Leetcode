# Catch Me if you can

Stripe processes billions of dollars worth of transactions every day. As 

guardians of the internet ecosystem, it is our duty to ensure that legitimate 

merchants can safely transact with their cucstomers, and that we quickly detect

and block illegitimate or fraudulent activity.

To detect fraud, we employ various ML models as scales such as Radar to detect

fraudulent transcations as they come in. These models examine a variety of 

different varaibles about incoming transcations to determine their authenticity.

One input we can look at is the outcome from the credit card networks like Visa

/Mastercard. These networks communicate with banks and provide different

response codes to reflect the outcomes of credit card transactions. While they 

act as a safety net, if we have enough data to determine a mercahnt is fradulent, 

we should proactively block them to protect consumers from malicious activities

like usage of stolen cards.

Today we will be build a very simple fraud detection model to determine if a merchant is fraudulent or not.

## Part 1

Each Stripe merchant has an associated Merchant Consumer Code (MCC) specifying

what kind of business the merchant operates. Certain businesses e.g. airlines,

event venues are more risky than others, so we have different tolerances of

fraud for them. We will start with a very basic algorithm for detecing fraud:

if a merchant is ever at or above a certain threshold of the total number of 

fraudulent transactions (all threshold are integers > 1), we will mark them

as fraudulent. We will additionally only begin marking merchants as fraudulent 

once we've seen at least some initial number of transactions total for them, to

prevent merchants as being marked fraudulent if the first couple transactions we

see from them are fraudulent.

There are five string inputs. First we will set up the scenario with:

- Input 1: a comma-separated list of codes that are not fraudulent

- Input 2: a comma-separated list of codes that are fraudulent 

- Input 3: a table of MCCs and their corresponding fraud thresholds (each row is separated by a newline and each column is separated by a comma)

- Input 4: A table of merchants by account ID and their corresponding MCC

- Input 5: The minimum number of transactions we have to have seen in order to evaluate a merchant as fraudulent or not

- Input 6: A table of charges that look like

  `CHARGE, charge_id, account_id amount, Code`

You will return a **lexicographically sorted c comma-separated list of merchants** (by account_id) that are fraudulent.

Example:

Input

``````
"approved", "invalid_pin", "expired_card"
"do_not_honor", "stolen_card", "lost_card"

retail, 5
airline, 2
restaurant, 10
venue, 3

acct_1, airline
acct_2, venue
acct_3, retail

0

CHARGE, ch_1, acct_1, 100, do_not_honor
CHARGE, ch_2, acct_1, 200, approved
CHARGE, ch_3, acct_1, 300, do_not_honor
CHARGE, ch_4, acct_2, 100, lost_card
CHARGE, ch_5, acct_2, 200, lost_card
CHARGE, ch_6, acct_2, 300, lost_card
CHARGE, ch_7, acct_3, 100, lost_card
CHARGE, ch_8, acct_2, 200, stolen_card
CHARGE, ch_9, acct_3, 100, approved
``````



Output

``````
acct_1, acct_2
``````

In the example above, we see that the initial transaction mininum is 0 transactions, so we can immediately begin evaluating merchants. We see that `acct_1` has 2 transactions marked as `do_not_honor`. It has an MCC code airline, so it has a fraud threshold of 2 fraudulent transactions. So, this merchant is marked as fraudulent by our algorithm. Similarly, acct_2, a venue merchant by MCC code, has 4 fraudulent transactions, which is above the threshold of 3 for this MCC code. On the other hand, acct_3 only has 1 fraudulent transaction, which is below its threshold of 5, so we don't mark it as fraudulent.

## Part 2

We deployed this model to production, but now we're getting complaints from large users like Ticketmaster and Amazon that have a large number of transactions and are being marked as fraudulent even though most of their transactions are legitimate. Using a numerical threshild is too strict, so we will create a new algorithm that uses the percentage of fraudulent transactions (between 0 and 1, inclusive) as our threshold. If a merchant's fraud percentage is ever at or above this threshold, they will be marked as fraudulent and remian fraudulent even if their percentage drops with more transactions. We will once again have a minimum number of transcations to see before evaluating merchants.



We will have the same 6 inputs but the threashold will now be a fraction representing the maximum percentage of fraudulent transactions allowed before a merchant is marked as fraudulent. The output will again be a list of merchants taht are fraudulent.



Example

Input

``````
"approved", "invalid_pin", "expired_card"
"do_not_honor", "stolen_card", "lost_card"

retail, 0.5
airline, 0.25
restaurant, 0.8
venue, 0.25

acct_1, airline
acct_2, venue
acct_3, venue

0

CHARGE, ch_1, acct_1, 100, do_not_honor
CHARGE, ch_2, acct_1, 200, approved
CHARGE, ch_3, acct_1, 300, do_not_honor
CHARGE, ch_4, acct_2, 400, approved
CHARGE, ch_5, acct_2, 500, approved
CHARGE, ch_6, acct_1, 600, lost_card
CHARGE, ch_7, acct_2, 700, approved
CHARGE, ch_8, acct_2, 800, approved
CHARGE, ch_9, acct_3, 800, approved
CHAREG, ch_10, acct_3, 700, approved
CHARGE, ch_11, acct_3, 600, approved
CHARGE, ch_12, acct_3, 500, stolen_card
CHARGE, ch_13, acct_3, 500, stolen_card
CHARGE, ch_14, acct_2, 400, stolen_card
``````

Output 

acct_1, acct_3

For acct_1, we consider the ratio once we encounter ch_3. The first 3 charges have 2 fraudulent charges and 1 non-fraudulent charge, so the ratio is 0.66, which is above the fraud threshold of 0.25 since it is an airline. So, this merchant is marked as fraudulent.

For acct_2, its first four charges are all approved. When we encounter its first fraudulent charge, ch_14, it already has 3 non-fraudulent charges, which makes the fraud ratio 0.2, below the threshold of 0.25.

For acct_3, its third charge is ch_11. At this point, the ratio is 0. The next two charges are fraudulent, however, so the fraud ratio is 0.4 by the end of the charge list. This is above the threshold of 0.25, so we mark this merchant as fraudulent.



## Part 3

Our fraud detection model is now working quite well in the wild given the information we receive from the card network. However, merchants have complained that some of these transactions are incorrectly being marked as fraudulent by the credit card netoworks. To address this concern, we have given merchants the ability to dispute transactions that were marked as fraudulent. This overturns the "fraudulent" status of a transaction. If a merchant is amrked as fraudulent by transaction that was disputed, that merchantt's status may be restored until they subsequently meet the minimum fraud criteria again. This is the only way that their status can be restored.

These disputes will be provided in the input as follows:

`DISPUTE, charge_id`

Input

``````
"approved", "invalid_pin", "expired_card"
"do_not_honor", "stolen_card", "lost_card"
retail,0.8
venue,0.25

acct_1,retail
acct_2,retail

2

CHARGE,ch_1,act_1,100,do_not_honor
CHARGE,ch_2,acct_1,200,lost_card
CHARGE,ch_3,acct_1,300,do_not_honor
DISPUTE,ch_2
CHARGE,ch_4,acct_2,400,lost_card
CHARGE,ch_5,acct_2,500,lost_card
CHARGE,ch_6,acct_1,600,lost_card
CHARGE,ch_7,acct_2,700,lost_card
CHARGE,ch_8,acct_2,800,do_not_honor
``````

output

acct_2

In the provided example, both accounts have retial MCCs with a mininum total transaction count of 2 and minimum fraud ratio of 0.8. If we examine just the first three charges, acct_1 meets our fraudulent conditions by ch_3. However, due to the dispute, we no longer mark ch_2 as fraudulent, so the merchant no longer meets our condition for fraud.

Let's break this down. By the second charge(ch_2), this merchant meets the criteria for fraud, since there are now at least 2 transactions and a fraud ratio of 1.0. However, since it is later successfully disputed, we treat it as a non-fraudulent transactionl. This means that although this third charge(ch_3) is also fraudulent, their fraud ratio is actually still about 0.66, below the minimum threshold of 0.8. When they later process their fourth charge(ch_6), their fraud ratio goes up to 0.75, still below the mininum threshold.

On the ohter hand, since all transactions of acct_2 were fraudulent, they quickly meet our minimum  requirements for being marked as fraudulent.





















































