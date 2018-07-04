class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        while True:
            fallen = dominoes.replace("R.L", "S")
            fallen = fallen.replace(".L", "LL").replace("R.", "RR")

            if fallen == dominoes:
                break
            else:
                dominoes = fallen
        
        return dominoes.replace("S", "R.L")
