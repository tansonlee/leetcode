class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(s):
            res = []
            sep = list(map(int, list(curr)))
            for i in range(len(s)):
                sep[i] = (sep[i] + 1) % 10
                res.append(("".join(map(str, sep)), depth + 1))
                sep[i] = (sep[i] - 2) % 10
                res.append(("".join(map(str, sep)), depth + 1))
                sep[i] = (sep[i] + 1) % 10
            return res
        
        deadends = set(deadends)
        q = collections.deque([("0000", 0)])
        visited = set()

        while q:
            curr, depth = q.popleft()
            if curr in deadends or curr in visited:
                continue
            if curr == target:
                return depth
            visited.add(curr)
            
            for n in neighbors(curr):
                q.append(n)
                
        return -1

