# 844. Backspace String Compare

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_stack = []
        t_stack = []

        for letter in S:
            if letter == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(letter)
            
        for letter in T:
            if letter == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(letter)
        
        return (s_stack == t_stack)
