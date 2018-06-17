# 187. Repeated DNA Sequences
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        counters = {}

        for i in range(len(s) - 9):
            sub_code = s[i:i + 10]
            if sub_code not in counters: counters[sub_code] = 1
            else: counters[sub_code] += 1
            
        return [subcode for subcode in counters if counters[subcode] > 1]
