class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        i = 0
        while i < len(bits):
            if bits[i] == 1 and (i + 1) == len(bits) - 1:
                return False
            if bits[i] == 1 and (i + 1) <= len(bits) - 1:
                i += 1
            i += 1
            
        return True
