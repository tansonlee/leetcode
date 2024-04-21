class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        def dfs(curr, visited):
            if curr == destination:
                return True
            visited.add(curr)
            for n in g[curr]:
                if n not in visited:
                    if dfs(n, visited):
                        return True
            return False
        
        return dfs(source, set())
        

                
        
