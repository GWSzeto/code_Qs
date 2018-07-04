class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        if n > 1 and n % 2 != 0: return n
        
        for i in range(n):
            if n % 2**i == 0 and n % 2**(i + 1) != 0:
               return "fuck" 