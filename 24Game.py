from operator import truediv, add, sub, mul

class Solution(object):
    def judgePoint24(self, nums):
        if len(nums) == 1: return abs(nums[0] - 24) < 1e-6
        
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if i != j:
                    # generating a list of all the left over elements
                    leftover = [nums[k] for k in xrange(len(nums)) if i != k != j]
                    for oper in (truediv, add, sub, mul):
                        # skip redundant operations
                        if (oper is add or oper is mul) and j > i: continue
                        # avoiding division by zero
                        if oper is not truediv or nums[j]:
                            leftover.append(oper(nums[i], nums[j]))
                            if self.judgePoint24(leftover): 
                                return True
                            leftover.pop()
        return False