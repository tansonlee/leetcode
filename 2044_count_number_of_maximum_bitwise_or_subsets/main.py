class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for n in nums:
            max_or |= n
        
        result = 0
        for mask in range(2 ** len(nums)):
            curr = 0

            for i in range(len(nums)):
                if (mask >> i) & 1:
                    curr |= nums[i]
            
            if curr == max_or:
                result += 1
        
        return result
        
