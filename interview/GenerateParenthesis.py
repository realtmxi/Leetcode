# 小红书安卓客户端开发 二面
# Leetcode 22 - Generate Parentheses

# Given n pairs of parenthese, write a function to generate all combinations of well-formed parentheses.

# Example 1:
# Input: n = 3
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        