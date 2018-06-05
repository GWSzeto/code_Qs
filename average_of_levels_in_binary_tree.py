# 637. Average of Levels in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__( x):
#         val = x
#         left = None
#         right = None

class Solution:
    def average(self, level, avg_list, node):
        if node is None:
            return avg_list
        if len(avg_list) <= level:
            avg_list.append([node.val, 1])
        else:
            avg_list[level][0] += node.val
            avg_list[level][1] += 1
        avg_list = self.average(level + 1, avg_list, node.left)
        avg_list = self.average(level + 1, avg_list, node.right)

        return avg_list

    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        avg_list = self.average(0, [], root)
        avg_list = [level[0]/level[1] for level in avg_list]
        
        return avg_list
        