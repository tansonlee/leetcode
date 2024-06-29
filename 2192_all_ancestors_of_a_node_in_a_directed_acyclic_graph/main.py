class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        back_edges = defaultdict(list)
        for a, b in edges:
            back_edges[b].append(a)
        
        result = [set() for _ in range(n)]
        def dfs(origin, node):
            if node in result[origin]:
                return
            result[origin].add(node)
            for neighbor in back_edges[node]:
                dfs(origin, neighbor)

        for i in range(n):
            for neighbor in back_edges[i]:
                dfs(i, neighbor)
        
        for i in range(len(result)):
            result[i] = sorted(list(result[i]))

        return result

        
