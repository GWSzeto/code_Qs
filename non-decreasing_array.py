# 665 Non-decreasing Array
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        change_index = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if change_index is not None:
                    return False
                change_index = i
        
        return (change_index is None or change_index == 0 or change_index == len(nums) - 2
                or nums[change_index - 1] <= nums[change_index + 1] or nums[change_index] <= nums[change_index + 2])