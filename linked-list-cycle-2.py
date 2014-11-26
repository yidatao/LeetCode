class Solution:
    # @param head, a ListNode
    # @return a list node
    # inspired by http://fisherlei.blogspot.hk/2013/11/leetcode-linked-list-cycle-ii-solution.html
    def detectCycle(self, head):
        p1 = head
        p2 = head
        while p1 != None and p2 != None:
            p1 = p1.next
            p2 = p2.next
            #p2 moves two nodes ahead
            if p2 != None:
                p2 = p2.next
            #two pointers meet.
            if p1 == p2:
                break

        if p2 == None:
            #no cycle
            return None

        #at this point, p2's step = x+my+k
        #p1's step = x+ny+k
        #p2's steps are twice p1's steps
        #so we have x+k=(m-2n)y, meaning x+k % y = 0
        #now we moved k. If we move x more nodes, we'll get to the beginning of the cycle
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p2


