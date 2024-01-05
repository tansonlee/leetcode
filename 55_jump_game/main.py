from functools import cache

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        
        return True

        # memoization
        # # can i get to index n
        # @cache
        # def helper(n):
        #     if n == 0:
        #         return True

        #     i = n - 1
        #     while i >= 0:
        #         if nums[i] >= (n - i) and helper(i):
        #             return True
        #         i -= 1
            
        #     return False
        
        # return helper(len(nums) - 1)

        # DP
        # dp = [False for _ in range(len(nums))]
        # dp[0] = True

        # for i, n in enumerate(nums):
        #     # Set the next n numbers in dp to be true.
        #     if dp[i] == False:
        #         continue
        #     for j in range(i + 1, i + n + 1):
        #         if j < len(dp):
        #             dp[j] = True
        
        # return dp[-1] == True
            
