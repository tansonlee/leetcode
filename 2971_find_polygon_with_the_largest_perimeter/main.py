class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        cumulative_sum = 0
        result = 0
        index = 0
        for i in range(len(nums)):
            if nums[i] < cumulative_sum:
                result = cumulative_sum + nums[i]
                index = i
            cumulative_sum += nums[i]

        if index < 2:
            return -1
        
        return result

