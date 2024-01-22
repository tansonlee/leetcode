class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = 0
        result = None
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] < 0:
                result = abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
            s += abs(nums[i])
        
        n = len(nums)

        return [result, (n * (n + 1)) // 2 - s + result]
        
