# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    # check the illustration: http://www.cnblogs.com/zuoyuan/p/3745126.html
    def copyRandomList(self, head):
        if head is None: return None
        p = head
        #insert same content node
        while p:
            pnew = RandomListNode(p.label)
            pnew.next = p.next
            p.next = pnew
            p = pnew.next
        #copy random pointer
        p = head
        while p:
            if p.random:
                #p.random.next is the newly insert same value node last step
                p.next.random = p.random.next
            p = p.next.next
        #split the list
        p1 = head
        head2 = head.next
        p2 = head2
        while p2.next:
            p1.next = p2.next
            p2.next = p2.next.next
            p1 = p1.next
            p2 = p2.next
        p1.next = None
        p2.next = None
        return head2