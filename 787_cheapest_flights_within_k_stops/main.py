import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Construct graph
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))
        
        # bfs/dijkstras
        curr = [(0, src, 0)]
        visited = {}
        while len(curr) > 0:
            cost, node, hops = heapq.heappop(curr)
            if node == dst:
                return cost
            
            if hops >= k + 1:
                continue
            
            if node in visited and visited[node] <= hops:
                continue
            
            visited[node] = hops
            
            for n_node, n_cost in graph[node]:
                heapq.heappush(curr, (cost + n_cost, n_node, hops + 1))
        
        return -1


