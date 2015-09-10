# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    # Time limit exceeded
    def reorderList0(self, head):
        p1 = head
        while p1 != None:
            p2 = p1.next
            p3 = p1
            p4 = p2
            while p4 != None and p4.next != None:
                p4 = p4.next
                p3 = p3.next
            if p2 == p4:
                break
            p1.next = p4
            p4.next = p2
            p3.next = None
            p1 = p2
        return head

    def reorderList1(self, head):
        if head == None or head.next == None or head.next.next == None:
            return head

        #split list to two equal sized parts
        #fast moves two steps while slow moves 1 step
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        #reverse the second part
        last = None
        cur = l2
        while cur:
            next = cur.next
            cur.next = last
            last = cur
            cur = next
        l3 = last

        #merge two parts
        #since either size of l1 and l3 are equal, or l1's size is 1 element larger than l3 if head contains odd numbers of elements, l3 will reach the end first
        while l3:
            t1 = l1.next
            t3 = l3.next
            l1.next = l3
            l3.next = t1
            l1 = t1
            l3 = t3

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(Solution().reorderList(head))