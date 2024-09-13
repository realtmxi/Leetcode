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
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
            result = max(result, dp[i])
        return result