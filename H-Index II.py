class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        length = len(citations)           
        start = 0
        end = len(citations)

        while start < end:
            mid = (start + end)//2
            if citations[mid] >= length - mid:
                end = mid
            else:
                start = mid + 1
        
        return length - start
            