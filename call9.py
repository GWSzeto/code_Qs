"""
      5
    /    \
  7      3
         /\
       1    2
       /
      4
"""
def traversal(node):
    def findDepth(mode, node, depth):
        left = findDeepest(node.left, depth + 1) if node.left else depth
        right = findDeepest(node.right, depth + 1) if node.right else depth

        return max(left, right) if mode == "deepest" else min(left, right)
    
    deepest = findDepth("deepest", node, 0)
    shallowest = findDepth("shallowest", node, 0)

    return deepest - shallowest


