class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        valid_num = -1
        for n in nums:
            if n > 0 and n <= len(nums):
                valid_num = n
                break
        
        if valid_num == -1:
            return 1
        
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = valid_num
        
        for n in nums:
            nums[abs(n) - 1] = abs(nums[abs(n) - 1]) * -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1
