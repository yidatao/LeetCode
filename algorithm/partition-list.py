# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        smaller = ListNode(0)
        p1 = smaller
        larger = ListNode(0)
        p2 = larger
        while head != None:
            if head.val < x:
                p1.next = ListNode(head.val)
                p1 = p1.next
            else:
                p2.next = ListNode(head.val)
                p2 = p2.next
            head = head.next
        p1.next = larger.next #append two lists
        return smaller.next #ignore the initial dummy node

head = ListNode(1)
head.next = ListNode(1)
print(Solution().partition(head,0))