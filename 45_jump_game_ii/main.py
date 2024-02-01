class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf") for _ in range(len(nums))]
        dp[0] = 0

        for i in range(len(nums)):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]
