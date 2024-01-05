class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        m = {}
        for a, b in paths:
            m[a] = b
        
        curr = paths[0][0]
        while True:
            if curr not in m:
                return curr
                break
            curr = m[curr]
        
