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
        result = []
        def backtrack(temp, left, right):
            if len(temp) == 2 * n:
                result.append("".join(temp))
                return
            if left < n:
                temp.append("(")
                backtrack(temp, left+1, right)
                temp.pop()
            if right < left:
                temp.append(')')
                backtrack(temp, left, right + 1)
                temp.pop()
        backtrack([], 0, 0)
        return result