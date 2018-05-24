class Solution(object):
    def lengthOfLongestSubstring(self, s):
        length = len(s)
        chars_storage = {}
        counter = 0
        i = 0

        for j, char in enumerate(s):
            if char in chars_storage:
                i = max(chars_storage[char] + 1, i)
            chars_storage[char] = j
            counter = max(counter, j - i + 1)
        
        return counter