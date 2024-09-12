# Leetcode 376 Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/description/

class Solution:
    # dp method: time complexity O(n^2), space complexity O(n)
    def wiggleMaxLength(self, nums):
        # dp[i][0]: ith is the longest increasing sequence
        # dp[i][1]: ith is the longest descreasing sequence
        # dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        # dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        dp = []
        for i in range(len(nums)):
            dp.append([1, 1])
            for j in range(i):
                if nums[j] > nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                if nums[j] < nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[-1][0], dp[-1][1])