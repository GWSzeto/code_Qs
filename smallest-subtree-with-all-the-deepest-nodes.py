def subtreeWithAllDeepest(root):
    stack = [root]
    deeptest = 0
    solution = [root.val]
    while stack:
        node = stack.pop()
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)class Solution(object):
    def subtreeWithAllDeepest(self, root):
        # Tag each node with it's depth.
        depth = {None: -1}
        def dfs(node, parent = None):
            if node:
                depth[node] = depth[parent] + 1
                dfs(node.left, node)
                dfs(node.right, node)
        dfs(root)

        max_depth = max(depth.itervalues())

        def answer(node):
            # Return the answer for the subtree at node.
            if not node or depth.get(node, None) == max_depth:
                return node
            L, R = answer(node.left), answer(node.right)
            return node if L and R else L or R

        return answer(root)
        

