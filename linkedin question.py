class Solution(object):
    # adding a node to the max heap
    def addPoint(self, point, k_closest, heap_len):
        k_closest.append(point)
        child_i = heap_len - 1
        parent_i = (heap_len - 2)//2
        while k_closest[child_i][0] > k_closest[parent_i][0]:
            old_parent = k_closest[parent_i]
            k_closest[parent_i] = k_closest[child_i]
            k_closest[child_i] = old_parent
            child_i = parent_i
            parent_i = (child_i - 2)//2

    # replacing a node in the max heap
    def replacePoint(self, point, k_closest):
        k_closest[0] = point
        parent = 0
        child = 1 if k_closest[1][0] > k_closest[2][0] else 2
        while k_closest[parent][0] < k_closest[child][0]:
            old_parent = k_closest[parent]
            k_closest[parent] = k_closest[child]
            k_closest[child] = old_parent
            parent = child
            child = parent*2 + 1 if k_closest[parent*2 + 1][0] > k_closest[parent*2 + 2][0] else parent*2 + 2


    # for a 2d plot, find the k nearest points to p
    def findKNearest(self, points, k, p):
        k_closest = []
        heap_len = 0
        px, py = p

        for x, y in points:
            length = abs(px - x)**2 + abs(py - y)**2
            if not k_closest:
                k_closest.append([length, x, y])
            if length < k_closest[0][0] and heap_len < k:
                heap_len += 1
                self.addPoint([length, x, y], k_closest, heap_len)
            if length < k_closest[0][0] and heap_len >= k:
                self.replacePoint([length, x, y], k_closest)
        
        return [[x, y] for _, x, y in k_closest]

s = Solution()
points = [[1, 2], [4, 3], [5, 8], [9, 2], [-1, -3]] 
print(s.findKNearest(points, 3, [6, 3]))