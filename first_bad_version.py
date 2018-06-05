# 278. First Bad Version

def isBadVersion(version):
    print("asdasd")

class Solution(object):
    def binary_search(self, start, end):
        if (end - start) <= 1:
            return start if isBadVersion(start) else end
        
        mid = (start + end)/2
        if isBadVersion(mid):
            return self.binary_search(start, mid)
        else:
            return self.binary_search(mid + 1, end)
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.binary_search(1, n)

