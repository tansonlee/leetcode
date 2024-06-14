class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()

        curr_min = -1
        result = 0
        for n in nums:
            curr_min = max(n, curr_min + 1)
            result += (curr_min - n)
        return result
        
