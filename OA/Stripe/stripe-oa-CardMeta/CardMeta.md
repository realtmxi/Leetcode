# Card Range Obfuscation

Payment card numbers are composed of eight to nineteen digits, the leading six

of which are referred to as the bankidentification number (BlN). Stripe's 

card metadata APl exposes information about different card brands within each 

BIN range, by returning a mapping of card intervals to brands.

However, a given BIN range may have gaps at the beginning, middle, or end of

the range where no vliad cards are present. This information can be used by

fraudsters to test for valid credit cards with a hign degree of probability.

To prevent fraudsters from abusing the data gaps, we must fill in missing  

values by extending the returned intervals to cover the entire range.

A BIN range refers to all the 16-digit card numbers starting with a given BIN:

for example, a BIN of 424242 has a range of 4242420000000000 to 

4242429999999999, inclusive.

An interval is a subset of a BIN range, also inclusive.

In this problem, we'll be taking as input a 6-digit BIN and a list of 10-digit

intervals within the BIN range corresponding to brands. We'll return a list

of sorted intervals covering the entire BIN range(i.e. for a BIN of 424242,

covering 4242420000000000 to 4242429999999999, inclusive).

Input format

Your input will consist of one line containing a 6-digit integer BIN, followed

one line containing a positive integer N, and N lines containing intervals and

their corresponding brands. 

The format of each interval is start, end, brand, where start and end are the

10 digits following the input BIN, and brand is an alphanumeric string.

Example:

```
777777
2
1000000000,3999999999,VISA
4000000000,5999999999,MASTERCARD
```

Output format

Your output will consist of one or more lines containing resulting intervals

and their corresponding brands. The output intervals should be sorted by start.

``````
7777770000000000,7777773999999999,VISA
7777774000000000,7777779999999999,MASTERCARD
``````

Formatting Note:

For most langaugees, Hackerrank will provide you with a code stub and a function to implement



## Part 1

For the first set of testcases, you'll be given a set of non-overlapping

intervals with no he lower end and/or higher end of the BIN range.

You're expected to extend the lowest internal to the lower boundary of the BIN

range, and the highest interval to the higher boundary of the BIN range.

This will sufficient to solve the first 4 test cases.

![image-20241014215210651](/Users/tianmuxin/Library/Application Support/typora-user-images/image-20241014215210651.png)

Example 1:

the VISA interval was extended on the higher end to fill the gap, up to the

Mastercard interval.

Input:

```
424242
1
5000000000,6555555555,VISA
```

Output

``````
4242420006000000,4242429999999999,VISA
``````

Example 2:

The Visa internal was extended on the lower end and the Mastercard interval was extended on the higher card.

``````
Input:
424242
2
4000000000,8999999999, MASTERCARD
1000000000,1999999999, VISA
Output:
4242420000000000,4242423999999999,VISA
4242424000000000,4242429999999999, MASTERCARD
``````



## Part2

For the second set of testcases, the set of non-overlapping intervals can also contain gaps in between know intervals. In these cases, the interval on the lower end o











424242

2

0000000000, 3700000000, VISA

6100000000, 9999999999, MASTERCARD

Output:

42424200000000000, 4242426099999999, VISA

42424261000000000, 4242429999999999, MASTERCARD

Example 2: the VISA interval is entended on the higher end to fill the gap up

to the Mastercarfd interval. The mastercard interval is extended on the higher

end to fill the gap up to the Amex Interval. The VISA interval extended on the

lower end following the requirements in 