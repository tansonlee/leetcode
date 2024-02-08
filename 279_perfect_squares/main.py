from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while True:
            if i * i > n:
                break
            squares.append(i * i)
            i += 1
        
        # Bottom up approach
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, len(dp)):
            for s in squares:
                if s > i:
                    break
                dp[i] = min(dp[i], dp[i - s] + 1)
        
        return dp[n]

        # Top down approach
        @cache
        def helper(n):
            if n == 0:
                return 0

            result = float("inf")
            for s in squares:
                if s > n:
                    break
                result = min(result, helper(n - s) + 1)
            return result
        
        return helper(n)
        
