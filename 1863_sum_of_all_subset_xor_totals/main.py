class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        
        def subsets(remaining, curr, xor):
            nonlocal result
            if len(remaining) == 0:
                result += xor
                return
            
            subsets(remaining[1:], curr + [remaining[0]], xor ^ remaining[0])
            subsets(remaining[1:], curr, xor)
        
        subsets(nums, [], 0)
        return result
        
