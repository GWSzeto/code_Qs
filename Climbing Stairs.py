# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0: return 0

        back_log = [0, 1]

        for _ in range(n):
            back_log[1] = sum(back_log)
            back_log[0] = back_log[1] - back_log[0]
        
        return back_log[1]
