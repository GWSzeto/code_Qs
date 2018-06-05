class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = len(nums)
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                start = i
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if i - 1 >= 0 and nums[i] < nums[i - 1]:
                end = i
                break
        
        return (end - start + 1)
