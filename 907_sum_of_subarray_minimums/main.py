from functools import cache

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = [0 for _ in range(len(arr))]
        result[0] = arr[0]

        stack = [0]

        for i in range(1, len(arr)):
            while len(stack) and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if len(stack) == 0:
                result[i] = (i + 1) * arr[i]
            else:
                j = stack[-1]
                result[i] = result[j] + (i - j) * arr[i]
            stack.append(i)
        
        return sum(result) % (10 ** 9 + 7)


        result = 0

        for i in range(len(arr)):
            curr_min = arr[i]
            for j in range(i, len(arr)):
                curr_min = min(curr_min, arr[j])
                result += curr_min
        
        return result % (10 ** 9 + 7)

        @cache
        def min_subarray(start, end):
            if start == end:
                return arr[start]
            return min(arr[end], min_subarray(start, end - 1))
        
        result = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                result += min_subarray(i, j)
        
        return result % (10 ** 9 + 7)



        # dp[i][j] = min(arr[i:j])
        # dp[i][j] = min(arr[j], dp[i][j - 1])

        dp = [[float("inf") for _ in range(len(arr))] for _ in range(len(arr))]

        for i in range(len(arr)):
            dp[i][i] = arr[i]
        
        curr_min = arr[0]
        for i in range(len(arr)):
            curr_min = min(curr_min, arr[i])
            dp[0][i] = curr_min
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                dp[i][j] = min(arr[j], dp[i][j - 1])
        
        result = 0
        for i in range(len(dp)):
            for j in range(i, len(dp[i])):
                result += dp[i][j]
        return result % (10 ** 9 + 7)
