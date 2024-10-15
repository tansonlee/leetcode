class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        swaps = 0

        for c in s:
            if c == '1':
                swaps += 1
            else:
                result += swaps

        return result
        
