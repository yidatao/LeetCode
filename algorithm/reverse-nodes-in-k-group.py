# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or head.next is None or k <= 1:
            return head
        #count the length of list
        length = 0
        p = head
        while p:
            length += 1
            p = p.next
        #check the # of groups
        groups = length / k
        #process (similar to reverse-linked-list-II)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        p = prev.next
        count = 1
        while count <= groups:
            #careful with the range, e.g., if k=2, only swap once, so range(k-1)
            for i in range(k-1):
                tmp = prev.next
                prev.next = p.next
                p.next = p.next.next
                prev.next.next = tmp
            count += 1
            prev = p
            p = prev.next
        return dummy.next
