# 402. Remove K Digits
class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        stack = []

        for digit in num:
            while stack and k and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        return "".join(stack[:-k or None]).lstrip("0") or "0"
