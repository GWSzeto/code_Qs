class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return len(nums) >= 2 and any(i == 0 and j == 0 for i, j in zip(nums, nums[1:]))

        sum = 0
        remainder_dict = {0: -1}
        for i in range(len(nums)):
            sum += nums[i]
            remainder = sum % k
            if remainder in remainder_dict and i - remainder_dict[remainder] >= 2:
                return True
            if remainder not in remainder_dict:
                remainder_dict[remainder] = i
            
        return False
        