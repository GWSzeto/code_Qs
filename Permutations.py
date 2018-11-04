class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(nums, path):
            if not nums:
                result.append(path)
            
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path + [nums[i]])
        
        dfs(nums, [])

        return result