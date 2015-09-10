class Solution:
    # @param two ListNodes
    # @return a ListNode
    # naive solution, also accepted
    def mergeTwoLists0(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val < l2.val:
            l = l1
            node1 = l1.next
            node2 = l2
        else:
            l = l2
            node1 = l1
            node2 = l2.next
        node = l
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next

        if node1 is not None:
            node.next = node1
        if node2 is not None:
            node.next = node2
        return l

    #recursion
    def mergeTwoLists1(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val < l2.val:
            l = l1
            l.next = self.mergeTwoLists1(l1.next,l2)
        else:
            l = l2
            l.next = self.mergeTwoLists1(l1,l2.next)
        return l