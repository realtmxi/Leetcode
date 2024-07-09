# Leetcode # 10 - Regular Expression Matching

"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".
"""

class Solution:
    def isMatchRecursion(self, s:str, p: str) -> bool:
        """
        Recursion solution
        """
        def helper(s, p, textIndex, patternIndex):
            # base case: if we have reached the end of the pattern
            if patternIndex == len(p):
                return textIndex == len(s)

            # check if the current character match of if the pattern has a '.'
            firstMatch = textIndex < len(s) and (s[textIndex] == p[patternIndex] or p[patternIndex] == '.')

            # check if the pattern has a '*'
            if patternIndex + 1 < len(p) and p[patternIndex + 1] == '*':
                return helper(s, p, textIndex, patternIndex + 2) or \
                    (firstMatch and helper(s, p, textIndex + 1, patternIndex))
            else:
                return firstMatch and helper(s, p, textIndex + 1, patternIndex + 1)

        return helper(s, p, 0, 0)


    def isMatchDP(self, s:str, p: str) -> bool:
        """
        Dynamic programming solution
        """

        rows, columns = len(s), len(p)
        # base case
        if rows == 0 and columns == 0:
            return True
        if columns == 0:
            return False
        # create a dp array
        dp = [[False for j in range(columns + 1)] for i in range(rows + 1)]
        dp[0][0] = True
        for i in range(2, columns + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]

        for i in range(1, rows+1):
            for j in range(1, columns+1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*' and j > 1:
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[rows][columns]


if __name__ == '__main__':
    s = Solution()
    print(s.isMatchRecursion("aa", "a*")) # True
    print(s.isMatchRecursion("ab", ".*")) # True
