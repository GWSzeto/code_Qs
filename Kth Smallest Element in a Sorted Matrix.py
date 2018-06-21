import heapq
import bisect

# the min heap assures that the smallest element is at the root of the tree.
# every subsequent node added will be greater than the root, that uses the fact that 
# it is sorted both in the row and the column. This effectively makes it so that the
# matrix is traversed in order.
class Solution1:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        n = len(matrix)
        pq = [[num, 0, i] for i, num in enumerate(matrix[0])]
        heapq.heapify(pq)
        print(pq)
        for _ in range(k - 1):
            print(pq)
            value, x, y = heapq.heappop(pq)
            if x == n - 1: continue
            heapq.heappush(pq, [matrix[x + 1][y], x + 1, y])
        
        return value

# uses binary search, but search space is the range, so instead of taking the value at index + 1
# actually just use the accumulated value to narrow down
class Solution2:
    def kthSmallest(self, matrix, k):
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if sum([bisect.bisect_right(row, mid) for row in matrix]) < k:
                low = mid + 1
            else:
                high = mid

        return low
        
s = Solution2()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 14, 15]
]
print(s.kthSmallest(matrix, 8))