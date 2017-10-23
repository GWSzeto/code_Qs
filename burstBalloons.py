"""
#312 Burst Balloons, leetcode
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
    (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
    (2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Uses dynamic programming to store the maximum score found between L(left) and R(right) so far and also uses divide and conquer by splitting down the last balloon popped and sectioning them off to the left and right
"""

class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + [value for value in nums if value > 0] + [1]
        len_num = len(nums)
        local_region = [[0]*len_num for _ in xrange(len_num)]

        for balloons_to_burst in xrange(1, len_num - 1):
            for L in xrange(0, len_num - balloons_to_burst - 1):
                R = L + balloons_to_burst + 1
                for M in xrange(L+1, R):
                    local_region[L][R] = max(local_region[L][R], local_region[L][M] + nums[L]*nums[M]*nums[R] + local_region[M][R]) 
        
        return local_region[0][-1]
