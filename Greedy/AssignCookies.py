# Leetcode 455 Assign Cookies
from typing import List

# Assume you are an awesome parent and want to give your children some cookies
# But you shoudl give each child at most one cookies.
# Each child i has a greed factor g[i], which is the minimum size of 
# a cookie that the child will be content with; and each cookie j has a
# size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i,
# and the child i will be content. You goal is to max the number of your
# content children.
class Solution:
    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        result = 0
        for i in range(len(s)):
            if g[result] <= s[i] and result < len(g):
                result += 1
        return result
    
    def findContentChildren2(self, g: List[int], s: List[int])-> int:
        g.sort()
        s.sort()
        index = len(s) - 1
        result = 0
        for i in range (len(g) - 1, -1, -1):
            if index >= 0 and s[index] > g[i]:
                result += 1
                index -= 1
        return result
