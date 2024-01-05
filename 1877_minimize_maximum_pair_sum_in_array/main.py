class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        result = -1
        mid = len(nums) // 2
        for i in range(mid):
            a = nums[i]
            b = nums[-i - 1]
            result = max(result, a + b)

        return result
        
