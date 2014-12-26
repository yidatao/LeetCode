# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    # This solution is from http://www.cnblogs.com/zuoyuan/p/3699508.html
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        #use slow (1 step per move) and fast (2 steps per move) to cut the list in the middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        l1 = head
        l2 = slow.next
        #don't forget this for l1 to be the first half
        slow.next = None
        l1 = self.sortList(l1)
        l2 = self.sortList(l2)
        return self.merge(l1, l2)

    #merge two list in ascending order
    def merge(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        dummy = ListNode(0)
        p = dummy
        #this merge puts elements in ascending order
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        #check the remaining (which is already sorted)
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next

