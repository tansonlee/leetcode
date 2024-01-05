class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        cumulative = [0 for _ in range(n)]
        cumulative[0] = nums[0]
        for i in range(1, n):
            cumulative[i] = cumulative[i - 1] + nums[i]
        
        result = [0 for _ in range(n)]
        for i in range(n):
            result[i] = 2 * (nums[i] * (i + 1)) - n * nums[i] - cumulative[i] + cumulative[n - 1] - cumulative[i]
        
        return result
        
