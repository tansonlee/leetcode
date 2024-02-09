from functools import cache

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        def satisfies(a, b):
            return a % b == 0 or b % a == 0

        #####
        # Top down approach
        #####
        @cache
        def helper(prev, index):
            if index == len(nums):
                return []
            
            result = []
            if satisfies(nums[index], prev):
                result = [nums[index]] + helper(nums[index], index + 1)
            
            x = helper(prev, index + 1)
            if len(x) > len(result):
                result = x
            return result
        
        return helper(1, 0)


        #####
        # Bottom up approach
        #####
        # build up dp
        dp = [1 for _ in range(len(nums))]
        dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if satisfies(nums[j], nums[i]):
                    dp[i] = max(dp[i], dp[j] + 1)

        # extract result from dp
        max_index = 0
        for i in range(len(dp)):
            if dp[i] > dp[max_index]:
                max_index = i

        result = [nums[max_index]]
        curr = max_index
        while True:
            if dp[curr] == 1:
                break
            
            for i in range(curr):
                if dp[i] == dp[curr] - 1 and satisfies(nums[i], nums[curr]):
                    result.append(nums[i])
                    curr = i
        
        return result[::-1]

