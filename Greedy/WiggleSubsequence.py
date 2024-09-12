# Leetcode 376 Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/description/

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) <= 1:
            return len(nums)
        curr_diff = 0
        prev_diff = 0
        result = 1
        for i in range(len(nums) - 1):
            curr_diff = nums[i+1] - nums[i]
            if (prev_diff <= 0 and curr_diff > 0) or (prev_diff >= 0 and curr_diff < 0):
                result += 1
                prev_diff = curr_diff
        return result
        