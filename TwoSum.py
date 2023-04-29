from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9)) # [0, 1]
    print(two_sum([3, 2, 4], 6)) # [1, 2]
    print(two_sum([3, 3], 6)) # [0, 1]

