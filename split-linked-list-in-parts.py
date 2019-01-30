def splitListtoParts(root, k):
    node = root
    length = 0
    while node != None:
        length += 1
        node = node.next

    divider = length // k
    remainder = length % k
   
    solution = [[] for _ in range(k)]
    node = root
    for sublist in solution:
        for _ in divider:
            sublist.append(node.val)
            node = node.next
        if remainder > 0:
            sublist.append(node.val)
            node = node.next
            remainder -= 1

    return solution


