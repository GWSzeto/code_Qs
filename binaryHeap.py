"""
how to make binary heaps, more specifically min heaps and the operations in python.
If a node is positioned at p, then its left child is at 2p and its right child is at 2p+1.
Similarly, to get the parent, divide by 2, it will always take the floor so the resulting
number is always the parent, regardless or left or right
"""
class BinHeap:
    def __init__(self):
        self.heapls = [0]

    # moves up new nodes until the heap structure is retored
    def moveUp(self, pos):
        while pos // 2 > 0:
            if self.heapls[pos] > self.heapls[pos//2]:
                temp = self.heapls[pos//2]
                self.heapls[pos//2] = self.heapls[pos]
                self.heapls[pos] = temp
            pos = pos // 2

    # inserts new nodes into the min heap and maintains structure
    def insert(self, val):
        self.heapls.append(val)
        self.moveUp(len(self.heapls) - 1)
    
    # moves down nodes until the heap structure is restored
    def moveDown(self, pos):
        length = len(self.heapls)
        while 2*pos <= length - 1:
            min_ = minNode(pos)
            if self.heapls[pos] > self.heapls[min_]:
                temp = self.heapls[min_]
                self.heapls[min_] = self.heapls[pos]
                self.heapls[min_] = self.heapls[pos]
           pos = min_
    
    # finds which node's child is the smallest
    def minNode(self, pos):
        if 2*pos+1 >= len(self.heapls):
            return 2*pos
        if self.heapls[2*pos] < self.heapls[2*pos+1]:
            return 2*pos
        else:
            return 2*pos+1

    # returns the root (smallest value) and then restores the structure of the heap
    def delMin(self):
        root = self.heapls[1]
        self.heapls[1] = self.heapls[len(self.heapls) - 1]
        self.heapls.pop()
        self.moveDown(1)


