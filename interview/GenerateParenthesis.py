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
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()
        backtrack([], 0, 0)
        return ans