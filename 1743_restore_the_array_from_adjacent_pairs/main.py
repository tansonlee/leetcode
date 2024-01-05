class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj = {}

        for a, b in adjacentPairs:
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            
            adj[a].append(b)
            adj[b].append(a)
        
        start = None
        for a in adj:
            if len(adj[a]) == 1:
                start = a
                break
        
        result = []
        curr = start
        prev = None

        while True:
            result.append(curr)
            if len(adj[curr]) == 1 and prev is not None:
                break
            nxt = adj[curr][0] if adj[curr][0] != prev else adj[curr][1]
            prev = curr
            curr = nxt
        
        return result
        
