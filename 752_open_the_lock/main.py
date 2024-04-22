class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        q = collections.deque([("0000", 0)])
        visited = set()

        while q:
            curr, depth = q.popleft()
            if curr in deadends:
                continue
            if curr in visited:
                continue
            if curr == target:
                return depth
            visited.add(curr)
            
            # try incrementing each
            sep = list(map(int, list(curr)))
            for i in range(len(sep)):
                sep[i] = (sep[i] + 1) % 10
                s = "".join(map(str, sep))
                q.append((s, depth + 1))
                sep[i] = (sep[i] - 1) % 10

                sep[i] = (sep[i] - 1) % 10
                s = "".join(map(str, sep))
                q.append((s, depth + 1))
                sep[i] = (sep[i] + 1) % 10
        
        return -1

