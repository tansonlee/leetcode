class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = longest LIS that ends at index i
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

