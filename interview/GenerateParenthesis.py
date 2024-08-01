# 小红书iOS客户端开发 二面
# Microsoft Suzhou SDE 一面
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
        