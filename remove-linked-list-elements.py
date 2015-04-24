# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head is None: return head
        dummy = ListNode(0)
        dummy.next = head
        p,q = dummy, head
        while q:
            if q.val == val:
                q = q.next
                p.next = q
            else:
                q = q.next
                p = p.next
        return dummy.next