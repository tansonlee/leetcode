class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        # 1 -> 1
        # 2 -> 2 + 1
        # 3 -> 3 + 2 + 1
        # 4 -> 4 + 3 + 2 + 1
        # n -> n * (n + 1) / 2

        counts = Counter(s)
        result = 0
        for char in counts:
            n = counts[char]
            result += (n * (n + 1)) // 2
        
        return result

        
