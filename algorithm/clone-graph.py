import collections

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # BFS
    def cloneGraph0(self, node):
        if node is None: return None
        queue = collections.deque([node])
        #key = original node, value = copied node
        visited = {}
        newNode = UndirectedGraphNode(node.label)
        visited[node] = newNode
        while queue:
            n = queue.popleft()
            neighbors = n.neighbors
            for ne in neighbors:
                #it's graph instead of tree. So node can already be visited
                if ne in visited:
                    #copy this neighbor
                    visited[n].neighbors.append(visited[ne])
                else:
                    newNE = UndirectedGraphNode(ne.label)
                    visited[ne] = newNE
                    visited[n].neighbors.append(newNE)
                    queue.append(ne)
        return newNode

    #DFS
    def cloneGraph(self, node):
        return self.cloneNode({}, node)

    def cloneNode(self, visited, node):
        if node == None:
            return None
        if node in visited:
            return visited[node]
        newNode = UndirectedGraphNode(node.label)
        visited[node] = newNode
        for ne in node.neighbors:
            newNode.neighbors.append(self.cloneNode(visited, ne))
        return newNode
