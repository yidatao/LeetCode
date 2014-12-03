class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head

        p1 = head
        length = 1
        while p1.next:
            p1 = p1.next
            length += 1

        if k % length == 0:
            return head
        else:
            k = k % length

        p2 = head
        i = 0
        while i < length - k - 1:
            p2 = p2.next
            i += 1

        l = p2.next
        p1.next = head
        p2.next = None

        return l

head = ListNode(1)
head.next = ListNode(2)
print(Solution().rotateRight(head,0))
