"""
You have k lists of sorted integers in ascending order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.
"""
import heapq
import sys

def smallestRange(nums):
    indicies = [0]*len*(nums)
    minHeap = []
    minRange = -sys.maxint - 1
    maxRange = sys.maxint 
    max_value = -sys.maxint - 1
    for ind in range(len(nums)):
        heapq.heappush(minHeap, (nums[i][0], i))
        max_ = max(max_, nums[i][0])
    
    while true:
        min_ = minHeap[0][1]
        min_value = minHeap[0][0]
        if maxRange - minRange > max_value - min_value:
            maxRange = max_value
            minRange = min_value
        indicies[min_] += 1
        if (indicies[min_] >= len(nums[min_])):
            break
        heapq.heapreplace(minHeap, (nums[min_][indicies[min_]], min_)
        max_value = max(max_value, nums[min_][indicies[min_]], min_)
    
    return (minRange, maxRange)


