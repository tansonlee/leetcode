class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        n = len(nums)

        result = 0
        i = 0
        while i < n:
            curr_val = nums[i]
            while i < n and nums[i] == curr_val:
                i += 1
            
            if i < n:
                result += i

        return result

