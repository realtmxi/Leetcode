# Leetcode 122 Best Time to Buy and Sell Stock II (medium)

# You are given an integer array prices where prices[i] is the
# price of a given stock on the ith day.
# On each day, you decide to buy and/or sell the stock.
# You can only hold at most one share of the stock at any time.
# However, you can buy it then immediately sell it on the same way.
# Find and return the maximum profit you can achieve.

# Example 1:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 7

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        for i in range(len(prices) - 1):
            if prices[i+1] - prices[i] > 0:
                result += prices[i+1] - prices[i]

        return result   