class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = [[] for _ in range(n)]
        for edge in edges:
            self.edges[edge[0]].append((edge[1], edge[2]))
        

    def addEdge(self, edge: List[int]) -> None:
        self.edges[edge[0]].append((edge[1], edge[2]))
        

    def shortestPath(self, node1: int, node2: int) -> int:
        # djikstras
        visited = [False for _ in range(self.n)]
        dists = [float("inf") for _ in range(self.n)]
        dists[node1] = 0

        for i in range(self.n):
            # Find the node to look at next -- min cost unvisited node
            min_cost = float("inf")
            min_cost_node = -1
            for n in range(self.n):
                if not visited[n] and dists[n] < min_cost:
                    min_cost = dists[n]
                    min_cost_node = n
            
            visited[min_cost_node] = True

            # Update adjacent nodes
            for neighbor, weight in self.edges[min_cost_node]:
                dists[neighbor] = min(dists[neighbor], dists[min_cost_node] + weight)
        
        return -1 if dists[node2] == float("inf") else dists[node2]


        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
