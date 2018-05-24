"""
#410 Split Array Largest Sum
Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays. Write an
algorithm to minimize the largest sum among these m subarrays.

solution uses binary search and greedy algorithm, you know that the answer
must lie between the largest element in the array and the sum of the whole
entire array, thus take the mid point and keep reassigning the left and 
right values to mid until left is greater than mid.

How do we reassign? We try to create as many subarrays as possible thats 
sum are smaller than mid. if the number of subarrays created is greater
than m, then mid is too small and we make r = mid - 1.

If we created less than or equal to m subarrays, then we have to make mid
smaller since we have to find the minimum sum, which is why we must keep
trying until l is greater than r, thats when the range between l and r
becomes so small that the difference becomes a matter of 1
"""

class Solution(object):
    def splitArray(self, nums, m):
        max_num = 0
        sum_nums = 0
        for num in nums:
            max_num = num if num > max_num else max_num
            sum_nums += num

        l = max_num
        r = sum_nums
        while l <= r:
            mid = (l+r)/2
            if self.valid(mid, nums, m):
                l = mid+1
            else:
                r = mid-1
        return l

    def valid(self, mid, nums, m):
        subarr_count = 1
        subarr_sum = 0
        for num in nums:
            subarr_sum += num
            if subarr_sum > mid:
                subarr_sum = num
                subarr_count += 1
                if subarr_count > m:
                    return True
        return False
