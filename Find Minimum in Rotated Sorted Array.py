# 153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1

        while start < end:
            if nums[start] < nums[end]:
                return nums[start]

            mid = (start + end) // 2

            if nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid
        
        return nums[start]