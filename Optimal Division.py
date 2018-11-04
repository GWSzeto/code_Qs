class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        nums = [str(num) for num in nums]
        if len(nums) <= 2:
            return "/".join(nums)

        return "{}/({})".format(nums[0], "/".join(nums[1:]))
