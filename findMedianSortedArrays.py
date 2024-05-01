from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        def _merge(arr1:List[int], arr2:List[int]) -> List[int]:
            i = 0
            j = 0
            result = []
            while i < len(arr1) and j < len(arr2):
                if arr2[j] > arr1[i]:
                    result.append(arr1[i])
                    i+=1
                else:
                    result.append(arr2[j])
                    j+=1
            while i < len(arr1):
                result.append(arr1[i])
                i+=1
            while j < len(arr2):
                result.append(arr2[j])
                j += 1

            return result

        arr = _merge(nums1, nums2)
        mid = len(arr) // 2
        if len(arr) % 2 != 0:
            return arr[mid]
        return (arr[mid-1] + arr[mid])/2
