from functools import cache

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for _ in range(len(arr))]

        for i in range(k):
            dp[i] = max(arr[:i+1]) * (i + 1)
        for i in range(k, len(arr)):
            for j in range(max(0, i - k + 1), i):
                dp[i] = max(dp[i], dp[j - 1] + max(arr[j:i + 1]) * (i - j + 1))
            dp[i] = max(dp[i], dp[i - 1] + arr[i])

        return dp[-1]

        @cache
        def helper2(start):
            if start == len(arr):
                return 0
            result = 0
            for i in range(1, min(k + 1, len(arr) - start + 1)):
                r = max(arr[start:start + i]) * i + helper2(start + i)
                result = max(result, r)
            return result
        
        return helper2(0)
            


        @cache
        def helper(prev, i, curr, curr_k):
            if i == len(arr):
                return prev + max(curr) * len(curr)
            if curr_k == 0:
                return helper(prev + max(curr) * len(curr), i + 1, (arr[i],), k - 1)
            if len(curr) == 0:
                return helper(prev, i + 1, curr + (arr[i],), curr_k - 1)

            case1 = helper(prev + max(curr) * len(curr), i + 1, (arr[i],), k - 1)
            case2 = helper(prev, i + 1, curr + (arr[i],), curr_k - 1)
            return max(case1, case2)
        
        return helper(0, 0, (), k)
        
