# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    # reference http://www.cnblogs.com/zuoyuan/p/3783342.html
    def reverseBetween(self, head, m, n):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head1 = dummy
        #head1 is ALWAYS the previous node of m
        for i in range(m - 1):
            head1 = head1.next
        #p is ALWAYS the node m
        p = head1.next
        for i in range(n - m):
            tmp = head1.next
            #reverse by switch node m's next to the front
            head1.next = p.next
            #adjust pointers
            p.next = p.next.next
            head1.next.next = tmp
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
print(Solution().reverseBetween(head, 2,4))