# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        if lists is None or len(lists) == 0:
            return None
        while len(lists) > 1:
            li = []
            #compare in pairs, otherwise TLE
            for i in range(0, len(lists)-1, 2):
                li.append(self.merge(lists[i], lists[i+1]))
            #odd len, the last list hasn't been merged, append it
            if len(lists) % 2 == 1:
                li.append(lists[-1])
            lists = list(li)
        return lists[0]

    def merge(self, list1, list2):
        dummy = ListNode(0)
        p = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p.next = list1
                list1 = list1.next
            else:
                p.next = list2
                list2 = list2.next
            p = p.next
        if list1:
            p.next = list1
        if list2:
            p.next = list2
        return dummy.next
