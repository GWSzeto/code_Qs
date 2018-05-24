class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        length = len(x)
        for i in range(length/2):
            if x[i] != x[length - i - 1]:
                return False
        
        return True
