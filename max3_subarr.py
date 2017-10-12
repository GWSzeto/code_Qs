"""
In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one. 
"""
ls = [1,2,1,2,6,7,5,1]
"""
Naive solution, double for loop through to grab sums, then triple for loop to brute force
find what the solution is
"""
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

"""
Optimal solution, use a window that is as long as the interval. Have it pass through
the list and the sum of that window will be appended to sums. then create 2 lists, left
and right which contains a list of the indicies of the largest sums so far. since the 
intervals are overlapping, the middle indicie must be between [K, len(sums)-K]. Traverse
through until the 3 largest indicies are found.
"""
def maxSumofThreeSubarrays(nums, K):
    sums = []
    window = 0
    # creates the array of sums
    for ind, num in enumerate(nums):
        window += num
        if ind >= K: window -= nums[ind-K]
        if ind >= K-1: sums.append(window)

    # creates a list of all the largest sums so far from the left
    left = [0] * len(sums)
    largest = 0
    for ind in range(len(sums)):
        if sums[ind] > sums[largest]:
            largest = ind
        left[ind] = largest

    # creates a list of all the largest sums so far from the right
    right = [0] * len(sums)
    largest = len(sums) - 1
    for ind in range(len(sums) - 1, -1, -1):
        if sums[ind] >= sums[largest]:
            largest = ind
        right[ind] = largest

    ans = None
    for j in range(K, len(sums) - K):
        i, k = left[j-K], right[j+K]
        if ans is None or \
        sums[i] + sums[j] + sums[k] > sums[ans[0]] + sums[ans[1]] + sums[ans[2]]:
                    ans = i, j, k

    return ans

print maxSumofThreeSubarrays(ls, 2)
