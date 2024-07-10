class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for l in logs:
            if l == '../':
                depth = max(depth - 1, 0)
            elif l == './':
                pass
            else:
                depth += 1
        return depth
        
