# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        l = ListNode(-1)
        p = l
        p1 = l1
        p2 = l2
        carry = 0
        while p1 and p2:
            sum = p1.val + p2.val + carry
            p.next = ListNode(sum % 10)
            p = p.next
            carry = sum / 10
            p1 = p1.next
            p2 = p2.next

        while p1:
            sum = p1.val + carry
            p.next = ListNode(sum % 10)
            p = p.next
            carry = sum / 10
            p1 = p1.next

        while p2:
            sum = p2.val + carry
            p.next = ListNode(sum % 10)
            p = p.next
            carry = sum / 10
            p2 = p2.next

        #don't forget this! The carry bit!!!
        if carry > 0:
            p.next = ListNode(carry)

        return l.next