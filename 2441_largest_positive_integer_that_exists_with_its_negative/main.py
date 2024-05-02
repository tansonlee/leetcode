class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        result = -1
        for n in nums:
            if n * -1 in s:
                result = max(result, abs(n))
        return result
        
