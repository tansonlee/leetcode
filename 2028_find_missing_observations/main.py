class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        curr_count = len(rolls)
        curr_total = sum(rolls)
        remaining = mean * (curr_count + n) - curr_total

        if remaining / 6 > n or remaining < n:
            return []
        
        result = [1] * n
        remaining -= n

        for i in range(len(result)):
            if remaining == 0:
                break
            
            take = min(remaining, 5)
            result[i] += take
            remaining -= take
        
        return result

