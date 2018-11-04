class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        people.sort(key=lambda (h, k) : (-h, k))

        result = []

        for p in people:
            result.insert(p[1], p)
        
        return result


        
