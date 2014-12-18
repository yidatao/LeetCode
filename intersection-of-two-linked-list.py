# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        p1,p2 = headA, headB
        len1, len2 = 0, 0
        while p1 is not None:
            len1 += 1
            p1 = p1.next
        while p2 is not None:
            len2 += 1
            p2 = p2.next
        plong = headA if len1 > len2 else headB
        pshort = headA if len1 <= len2 else headB
        #let longer list to move |len1-len2| steps
        for i in range(abs(len1-len2)):
            plong = plong.next
        #then two pointers move together
        while plong is not None:
            if plong == pshort:
                return plong
            plong = plong.next
            pshort = pshort.next
        return None
