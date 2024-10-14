# Leetcode 55 Jump Game
# You are given an integer array nums. You are initially positioned
# at the array's first index, and each element in the array represents
# your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

from typing import List

class Solution:
    def canJump(self, nums: List[int]) ->bool:
        if len(nums) == 1:
            return True
        cover = 0
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i + nums[i], cover)
                if cover >= len(nums) - 1:
                    return True
        return False