class GraphNode:
    def __init__(self, x):
        self.val = x
        self.neighbors = []
        self.visited = False

    def dfs(self):
        print(self.val)
        self.visited = True
        for n in self.neighbors:
            if not n.visited:
                n.dfs()

    def bfs(self):
        print(self.val)
        queue = self.neighbors
        while queue:
            node = queue.pop(0)
            if not node.visited:
                print(node.val)
                node.visited = True
                queue += node.neighbors

class GraphOperation:
    def recursive_dfs(self, graph, start, visited=[]):
        print(start)
        visited.append(start)
        for n in graph[start]:
            if n not in visited:
                self.recursive_dfs(graph, n, visited)

    def iterative_dfs(self, graph, start):
        visited = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.append(node)
                stack += graph[node]

    def bfs(self, graph, start):
        visited = []
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node)
                visited.append(node)
                queue += graph[node]



graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
#GraphOperation().recursive_dfs(graph, 'B')
GraphOperation().bfs(graph, 'A')

# n1,n2,n3,n4,n5,n6 = GraphNode(1),GraphNode(2),GraphNode(3),GraphNode(4),GraphNode(5),GraphNode(6)
# n1.neighbors = [n2,n3,n4]
# n2.neighbors = [n5]
# n3.neighbors = [n5]
# n4.neighbors = [n6]
# n5.neighbors = [n6]
# n1.dfs()
# n1.bfs()
