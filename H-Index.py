class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        
        buckets = [0]*(len(citations) + 1)
        for value in citations:
            buckets_ind = value if value < len(citations) else len(citations)
            buckets[buckets_ind] += 1
        
        total = 0
        for i in range(len(buckets) - 1, -1, -1):
            total += buckets[i]
            if total >= i:
                return i
        