# Leetcode 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
        for i in range(startIndex, n + 1):
            path.append(i)
            self.backtracking(n, k, i+1, path, result)
            path.pop()

    def backtracking_opt(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
        for i in range(startIndex, n - (k - len(path)) + 2):
            path.append(i)
            self.backtracking_opt(n, k, i + 1, path, result)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,2))
