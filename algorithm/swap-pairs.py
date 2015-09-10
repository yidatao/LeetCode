# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    # This solution requires extra space
    def swapPairs0(self, head):
        if head == None or head.next == None:
            return head
        p = head
        l1 = ListNode(0)
        l2 = ListNode(0)
        p1 = l1
        p2 = l2
        odd = True
        while p:
            if odd:
                p1.next = ListNode(p.val)
                p1 = p1.next
            else:
                p2.next = ListNode(p.val)
                p2 = p2.next
            odd = not odd
            p = p.next

        p1 = l1.next
        p2 = l2.next
        res = ListNode(0)
        l = res
        while p1 and p2:
            tmp1 = p1.next
            tmp2 = p2.next
            l.next = p2
            l.next.next = p1
            l = l.next.next
            p1 = tmp1
            p2 = tmp2
        return res.next

    def swapPairs1(self, head):
        if head == None or head.next == None:
            return head
        #key is to add a dummy head node
        l = ListNode(0)
        l.next = head
        p = l
        while p.next and p.next.next:
            #notice this is a chain when swapping
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = tmp.next #move to the node before the next pair
        return l.next

    #recursive solution
    def swapPairs2(self, head):
        if head == None or head.next == None:
            return head
        remain = head.next.next
        res = head.next
        res.next = head
        head.next = self.swapPairs2(remain)
        return res

head = ListNode(1)
head.next = ListNode(2)
print(Solution().swapPairs(head))

