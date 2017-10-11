"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one. 
"""
ls = [1,2,1,2,6,7,5,1]
def max3(nums, k):
	sums = []
	for ind in range(len(nums) - (k - 1)):
		end = ind + k
		sums.append(sum(nums[ind:end]))
	largest = 0
	largest_nums = []
	length = len(sums)
	for ind1, val1 in enumerate(sums):
		place = ind1 + k
		if place < length:
			for ind2, val2 in enumerate(sums[place:], start=place):
				place = ind2 + k
				if place < length:
					for ind3, val3 in enumerate(sums[place:], start=place):
						if val1 + val2 + val3 > largest:
							largest = val1 + val2 + val3
							largest_nums = [ind1, ind2, ind3]
	return largest_nums

print max3(ls, 2)
