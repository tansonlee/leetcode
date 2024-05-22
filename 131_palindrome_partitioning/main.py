class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        result = []
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                suffix_partitions = self.partition(s[i:])
                for sp in suffix_partitions:
                    result.append([prefix] + sp)
        return result
        
