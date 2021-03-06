# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node1 = node2 = head

        for _ in range(n):
            node2 = node2.next
        
        if node2 is None:
            return head.next
        
        while node2.next:
            node1 = node1.next
            node2 = node2.next

        node1.next = node1.next.next

        return head
        