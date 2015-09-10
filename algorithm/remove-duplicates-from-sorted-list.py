class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates0(self, head):
        if head == None:
            return head
        val = head.val
        node = head.next
        l = ListNode(val)
        p = l
        while node != None:
            if node.val != val:
                val = node.val
                p.next = ListNode(val)
                p = p.next
            node = node.next
        return l

    def deleteDuplicates1(self, head):
        if head == None:
            return head
        val = head.val
        p1 = head
        p2 = head.next
        while p2 != None:
            if p2.val != val:
                val = p2.val
                p1.next = p2
                p1 = p1.next
            else:
                p1.next = None
            p2 = p2.next
        return head
