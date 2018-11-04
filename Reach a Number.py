import math

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        t = abs(target)
        n = math.floor(math.sqrt(2*t))
        while True:
            minus = ((n + 1) * n)/2 - t
            if minus >= 0:
                if minus % 2 == 0:
                    return int(n)
            
            n += 1
    