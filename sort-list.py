def sortList(head):
    first = head
    second = head.next if head else None

    while second != None:
        if first.val > second.val# merge sort, recursively 
def sortList(self, head):
    if not head or not head.next:
        return head
    # divide list into two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    # cut down the first part
    slow.next = None
    l = self.sortList(head)
    r = self.sortList(second)
    return self.merge(l, r)
    
# merge in-place without dummy node        
def merge(self, l, r):
    if not l or not r:
        return l or r
    if l.val > r.val:
        l, r = r, l
    # get the return node "head"
    head = pre = l
    l = l.next
    while l and r:
        if l.val < r.val:
            l = l.next
        else:
            nxt = pre.next
            pre.next = r
            tmp = r.next
            r.next = nxt
            r = tmp
        pre = pre.next
    # l and r at least one is None
    pre.next = l or r
    return head:
            first.val, second.val = second.val, first.val
            first = first.next
        else:
            second.val, first.val = first.val, second.val
            second = second.next




