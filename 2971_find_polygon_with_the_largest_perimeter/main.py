class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        cumulative_sum = [0 for _ in range(len(nums))]
        cumulative_sum[0] = nums[0]
        for i in range(1, len(nums)):
            cumulative_sum[i] = cumulative_sum[i - 1] + nums[i]

        result = 0
        for i in range(1, len(nums)):
            if nums[i] < cumulative_sum[i - 1]:
                result = i
        
        if result < 2:
            return -1
        
        return cumulative_sum[result]

