class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None:
            return False
        p1 = head
        p2 = head
        while True:
            #p2 moves forward two nodes each time
            for i in range(2):
                p2 = p2.next
                if p2 is None:
                    return False
            #p1 moves one node each time
            p1 = p1.next
            #if there is cycle, then p1 and p2 will finally meet
            if p1 == p2:
                return True
