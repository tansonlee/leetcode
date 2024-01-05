
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = {}
        for n in arr:
            if n not in counts:
                counts[n] = 0
            counts[n] += 1
        
        for n in counts:
            if counts[n] > len(arr) / 4:
                return n
        
