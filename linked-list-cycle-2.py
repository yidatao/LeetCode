class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        p2 = head
        p1 = head
        while True:
            for i in range(2):
                p2 = p2.next
                if p2 is None:
                    return None
                if p2 == p1:
                    return p1
            p1 = p1.next

