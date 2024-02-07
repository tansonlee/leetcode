class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        nums[0] = 1 if nums[0] == 1 else -1
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + (1 if nums[i] == 1 else -1)
    
        d = {}
        d[0] = -1
        result = 0
        for i in range(len(nums)):
            if nums[i] in d:
                result = max(result, i - d[nums[i]])
            else:
                d[nums[i]] = i
        
        return result

