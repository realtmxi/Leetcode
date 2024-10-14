# Leetcode 53 Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/

# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6

# Example 2:
# Input: nums = [1]
# Output: 1

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23

from typing import List

class Solution:
    def maxSubarray(self, nums: List[int])->int:
        result = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count <= 0:
                count = 0
        return result