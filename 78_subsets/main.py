class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(curr, remaining):
            nonlocal result
            if len(remaining) == 0:
                result.append(curr)
                return
            
            backtracking(curr + [remaining[0]], remaining[1:])
            backtracking(curr, remaining[1:])
        
        backtracking([], nums)
        return result
        
