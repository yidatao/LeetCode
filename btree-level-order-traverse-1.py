import Queue
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        list = []
        l = []
        q = Queue.Queue()
        q.put(root)
        q.put(None)
        while not q.empty():
            elem = q.get()
            if elem is None:
                list.append(l)
                l = []
            else:
                l.append(elem.val)
                q.put(elem.)
                