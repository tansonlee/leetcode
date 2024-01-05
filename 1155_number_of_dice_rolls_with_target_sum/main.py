from functools import cache

class Solution:
    @cache
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target <= 0:
            return 0
        if n == 0:
            return 0
        if n == 1:
            if target <= k:
                return 1
            return 0

        
        result = 0
        for roll in range(1, k+1):
            result += self.numRollsToTarget(n - 1, k, target - roll)
        
        return result % (10 ** 9 + 7)
