class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Find the node(s) with indegree 0

        indegrees = [0 for _ in range(n)]

        for a, b in edges:
            indegrees[b] += 1
        
        results = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                results.append(i)
        
        if len(results) != 1:
            return -1
        return results[0]
        
