class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_edge(self, u, v, bidirectional=True):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        if bidirectional:
            self.adj_list[v].append(u)
    
    def dfs(self, start):
        visited = set()
        print("DFS traversal starting from node", start)
        self._dfs_recursive(start, visited)
    
    def _dfs_recursive(self, node, visited):
        if node not in visited:
            print("Visiting node:", node)
            visited.add(node)
            for neighbor in self.adj_list.get(node, []):
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]
        print("BFS traversal starting from node", start)
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print("Visiting node:", node)
                visited.add(node)
                for neighbor in self.adj_list[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('B', 'C')
graph.add_edge('B', 'E')
graph.add_edge('D', 'E')
graph.add_edge('D', 'H')
graph.add_edge('D', 'G')
graph.add_edge('E', 'F')
graph.add_edge('E', 'C')
graph.add_edge('G', 'H')

print("DFS traversal:")
graph.dfs('A')

print("\nBFS traversal:")
graph.bfs('A')
