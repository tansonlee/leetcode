class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        result = []
        for i in range(len(nums)):
            ps = self.permute(nums[:i] + nums[i+1:])

            for p in ps:
                result.append([nums[i]] + p)
        
        return result

        
