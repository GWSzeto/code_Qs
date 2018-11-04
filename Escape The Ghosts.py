class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
        target_dist = abs(target[0]) + abs(target[1])

        for x, y in ghosts:
            ghost_dist = abs(target[0] - x) + abs(target[1] - y)
            if ghost_dist <= target_dist: return False
        
        return True
