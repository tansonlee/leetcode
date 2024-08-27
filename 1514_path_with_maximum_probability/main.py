class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Do Dijkstras

        # Construct adj list
        graph = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            graph[a].append((b, prob))
            graph[b].append((a, prob))

        heap = [(-1, start_node)]
        visited = set()

        while heap:
            prob, node = heappop(heap)
            if node == end_node:
                return prob * -1
            if node in visited:
                continue
            visited.add(node)
            
            for neighbor, neighbor_prob in graph[node]:
                heappush(heap, (prob * neighbor_prob, neighbor))
        
        return 0
        
