# Leetcode 27 Remove element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        while (fast < len(nums) - 1):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
