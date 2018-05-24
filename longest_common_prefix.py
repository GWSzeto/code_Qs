class Solution(object):
    def longestCommonPrefix(self, strs):
        longest_prefix = strs[0] if strs != [] else ""
        for string in strs[1:]:
            if longest_prefix == "":
                return ""
            new_longest_prefix = ""
            for chars in zip(longest_prefix, string):
                if chars[0] == chars[1]:
                    new_longest_prefix += chars[0]
                else:
                    break
            
            longest_prefix = new_longest_prefix
        
        return longest_prefix
                