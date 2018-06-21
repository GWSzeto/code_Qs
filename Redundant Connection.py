#684. Redundant Connection
class DSU(object):
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0]*1001

    # path compression algorithim, sets all the nodes in the sub graph to the root
    # so that it is faster lookup overall
    def findRoot(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.findRoot(self.parent[node])

        return self.parent[node]

    # union_by_rank optimization, makes the graph more shallow overall
    def union(self, node1, node2):
        node_root1 = self.findRoot(node1)
        node_root2 = self.findRoot(node2)
        if node_root1 ==  node_root2:
            return True
        elif self.rank[node_root1] > self.rank[node_root2]:
            self.parent[node_root2] = node_root1
            self.rank[node_root1] += self.rank[node_root2]
        elif self.rank[node_root1] < self.rank[node_root2]:
            self.parent[node_root1] = node_root2
            self.rank[node_root2] += self.rank[node_root1]
        else: 
            self.parent[node_root2] = node_root1
            self.rank[node_root1] += 1
        
        return False

class Solution(object):
    def findRedundantConnection(self, edges):
        ds = DSU()
        for edge in edges:
            if ds.union(*edge):
                return edge
