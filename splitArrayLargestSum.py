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
