# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        #pointer for exploring the list
        p1 = head
        dummy = ListNode(0)
        dummy.next = head
        #point to the last unique element
        p2 = dummy
        while p2.next:
            #p1 keeps moving if values are the same (note the list is sorted)
            while p1.next and p2.next.val == p1.next.val:
                p1 = p1.next
            #if p2's next is p1 after exploration, both move forward
            if p2.next == p1:
                p2 = p2.next
                p1 = p1.next
            else:
                #if p1 is farther away
                p2.next = p1.next
        return dummy.next


    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

x = ListNode(1)
x.next = ListNode(1)
x.next.next = ListNode(2)
Solution().printList(Solution().deleteDuplicates(x))