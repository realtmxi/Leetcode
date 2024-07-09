# leetcode 209 - Minimum Size Subarray Sum
from typing import List


class Solution:
    def brute_force(self, s: int, nums:List[int]) -> int:
        len = len(nums)
        min_len = float('inf')

        for i in range(len):
            sum = 0
            for j in range(i, len):
                sum += nums[j]
                if sum >= s:
                    min_len = min(min_len, j - i + 1)
                    break
        return min_len if min_len != float('inf') else 0

    def sliding_window(self, s: int, nums:List[int]) -> int:
        len = len(nums)
        left = 0
        right = 0
        min_len = float('inf')
        sum = 0

        while right < len:
            sum += nums[right]
            while sum >= s:
                min_len = min(min_len, right - left + 1)
                sum -= nums[left]
                left += 1
            right += 1

        return min_len if min_len != float('inf') else 0
