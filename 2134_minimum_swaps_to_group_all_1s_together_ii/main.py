class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        num_ones = 0

        for i in range(total_ones):
            num_ones += nums[i]
        
        result = total_ones - num_ones

        for i in range(total_ones, len(nums) + total_ones):
            num_ones -= nums[i - total_ones]
            num_ones += nums[i % len(nums)]
            result = min(result, total_ones - num_ones)
        
        return result

            
        
