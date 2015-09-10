class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head is None or head.next is None: return head
        prev, curr, nxt = head, head.next, head.next.next
        curr.next = prev
        prev.next = None
        prev = curr
        while nxt:
            curr = nxt
            nxt = nxt.next
            curr.next = prev
            prev = curr
        return curr