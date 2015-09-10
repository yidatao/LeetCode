#referred to https://github.com/Linzertorte/LeetCode-in-Python/blob/master/LRUCache.py
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def remove(self, node):
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.next.prev = node.prev
        node.prev.next = node.next

    def addFirst(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = node.next = None
            return
        self.head.prev = node
        node.next = self.head
        self.head = node
        node.prev = None

    def removeLast(self):
        self.remove(self.tail)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cursize = 0
        self.kmap = {} #{key,Node(key,value)}
        self.dlist = DoubleLinkedList()

    def set(self, key, value):
        if key in self.kmap: #O(1)
            self.dlist.remove(self.kmap[key]) #O(1)
            self.dlist.addFirst(self.kmap[key]) #O(1)
            self.kmap[key].val = value #O(1)
        else:
            node = Node(key, value)
            self.kmap[key] = node #O(1)
            self.dlist.addFirst(node) #O(1)
            self.cursize += 1
            if self.cursize > self.capacity:
                del self.kmap[self.dlist.tail.key] #O(1)
                self.dlist.removeLast() #O(1)
                self.cursize -= 1

    def get(self, key):
        if key in self.kmap: #O(1)
            self.dlist.remove(self.kmap[key]) #O(1)
            self.dlist.addFirst(self.kmap[key]) #O(1)
            return self.kmap[key].val
        return -1


# TLE
# class LRUCache:
#
#     capacity = 0
#     map = []
#     recency = 0
#     recency_map = []
#
#     # @param capacity, an integer
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#
#     # @return an integer
#     def get(self, key):
#         if key in map:
#             self.recency += 1
#             self.recency_map[key] = self.recency
#             return map[key]
#         return -1
#
#     # @param key, an integer
#     # @param value, an integer
#     # @return nothing
#     def set(self, key, value):
#
#         if key not in map and len(map) + 1 > self.capacity:
#             sorted(self.recency_map.items(), key = lambda x: x[1])
#             rkey = self.recency_map.keys()[0]
#             del self.recency_map[rkey]
#             del self.map[rkey]
#
#         self.recency += 1
#         self.recency_map[key] = self.recency
#         self.map[key] = value