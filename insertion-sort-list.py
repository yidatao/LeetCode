# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            #find a misplaced node
            if cur.next.val < cur.val:
                pre = dummy
                #find the insertion location
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
        return dummy.next