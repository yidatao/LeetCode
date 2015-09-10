# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next:
            #find a misplaced node
            if cur.next.val < cur.val:
                pre = dummy
                #find the insertion location
                while pre.next.val < cur.next.val:
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
        return dummy.next

    def insertionSortList1(self, head):
        if head is None or head.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        q = head.next
        while q:
            p = dummy
            while p.next.val < q.val:
                p = p.next
            if p.next != q:
                tmp = q.next
                q.next = p.next
                p.next = q
                q = tmp
            else:
                q = q.next
        return dummy.next

head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(4)
#head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(2)
sl = Solution().insertionSortList1(head)
while sl:
    print(sl.val)
    sl = sl.next
