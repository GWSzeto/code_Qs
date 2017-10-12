# Given a binary tree, return the postorder traversal of its nodes' values.

class TreeNode(object):
    def __int__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    ls = []
    def postord(self, root):
        if root:
            self.postord(root.left)
            self.postord(root.right)
            self.ls.append(root.val)
        return self.ls






