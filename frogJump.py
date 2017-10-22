class Solution(object):
    reached = False
    visited = None
    def canLeap(self, stones, pos, lastLeap):
        if pos == len(stones) - 1 or self.reached:
            self.reached = True
            return
        if (pos, lastLeap) in self.visited:
            return
        self.visited.add((pos, lastLeap))
        next_stone = pos + 1
        print pos, next_stone
        diff = stones[next_stone] - stones[pos]

        while diff <= lastLeap + 1:
            if diff >= lastLeap - 1:
                self.canLeap(stones, next_stone, diff)
            next_stone += 1
            if next_stone >= len(stones):
                break
            diff = stones[next_stone] - stones[pos]

    def canCross(self, stones):
        self.visited = set()
        if stones[1] - stones[0] != 1:
            return False
        self.canLeap(stones, 1, 1)
        return self.reached

test_list1 = [0,1,3,5,6,8,12,17]
test_list2 = [0,1,2,3,4,8,9,11]
test = Solution()
print test.canCross(test_list1)
print test.canCross(test_list2)
