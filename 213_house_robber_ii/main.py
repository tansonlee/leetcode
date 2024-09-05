class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber_i(nums):
            dp = [0] * len(nums)
    
            if len(nums) < 3:
                return max(nums)
    
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[2] + nums[0]
    
            for i in range(3, len(nums)):
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i]
            
            return max(dp[-1], dp[-2])
        
        if len(nums) == 1:
            return nums[0]
        
        # Do without the first number
        res1 = house_robber_i(nums[1:])

        # Do without the last number
        res2 = house_robber_i(nums[:-1])

        return max(res1, res2)
        
