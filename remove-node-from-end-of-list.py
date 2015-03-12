class Solution:
    # @return a ListNode
    def removeNthFromEnd0(self, head, n):
        if n == 0:
            return head
        temp = [] #store the entire list
        node = head
        while node is not None:
            temp.append(node)
            node = node.next

        if n == len(temp):
            if n == 1:
                return None
            #remove the first node
            head = temp[1]
        elif n == 1:
            #remove the last node
            temp[len(temp)-2].next = None
        else:
            temp[len(temp)-n-1].next = temp[len(temp)-n+1]
        return head

    #use two pointers, fast and slow
    def removeNthFromEnd1(self, head, n):
        fast = head
        for i in range(n):
            fast = fast.next

        slow = head
        if fast is not None:
            while fast.next is not None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next #here cannot use slow.next = fast, in case n = 1
            return head
        else:
            # remove the first node (n = len(list))
            return head.next


    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head is None or n == 0: return head
        count = 0
        p = head
        while p:
            count += 1
            p = p.next
        if count == n: return head.next
        p = head
        for i in range(count - n - 1):
            p = p.next
        p.next = p.next.next
        return head