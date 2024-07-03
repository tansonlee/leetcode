class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
            
        nums.sort()

        result = inf
        for i in range(4):
            result = min(result, nums[-i-1] - nums[3-i])

        return result
        
