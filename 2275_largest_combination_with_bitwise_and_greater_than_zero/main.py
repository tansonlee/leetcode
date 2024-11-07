class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        result = 0

        for bit in range(24):
            count = 0
            for n in candidates:
                if (n >> bit) & 1:
                    count += 1
            result = max(result, count)
        
        return result 
        
