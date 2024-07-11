# KMP Algorithm
from typing import List
class Solution:
    def compute_prefix_function(self, P, m) -> List[int]:
        pi = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and P[k+1] != P[i]:
                k = pi[k]
            if P[k+1] == P[i]:
                k += 1
            pi[i] = k 
        return pi


    def kmp_matcher(self, T: str, P: str) -> int:
        """
        T: text
        P: pattern
        m = len(P)
        n = len(T)
        """
        m = len(P)
        n = len(T)
        if m == 0:
            return 0
        
        pi = self.compute_prefix_function(P, m)
        j = 0

        for i in range(n):
            while j > 0 and T[i] != P[j]:
                j = pi[j - 1]
            if T[i] == P[j]:
                j += 1
            if j == m:
                return i - m + 1
        return -1
        


