# 22. Generate Parentheses
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        ans = []

        def buildBrackets(left = 0, right = 0, S = ""):
            if len(S) == n * 2:
                ans.append(S)
                return
            if left < n:
                buildBrackets(left + 1, right, S + "(")
            if right < left:
                buildBrackets(left, right + 1, S + ")")
        
        buildBrackets()
        return ans
            