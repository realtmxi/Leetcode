# Borderpass interview question
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        def backtrack(nums, path):
            if not nums:
                result.append(path)
                return

            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1:], path + [nums[i]])

        result = []
        backtrack(nums, [])
        return result
