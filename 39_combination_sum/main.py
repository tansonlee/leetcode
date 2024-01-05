class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # cache = {}

        def helper(target, lst):
            if target == 0:
                return []
            
            # if target in cache:
            #     return cache[target]

            # Try out all the candidates.
            possible = []
            for i, c in enumerate(lst):
                if target - c < 0:
                    continue
                
                if c == target:
                    possible.append([c])
                
                second_parts = helper(target - c, lst[i:])
                
                for sp in second_parts:
                    possible.append([c] + sp)
            
            # cache[target] = possible

            print(f"Ans for {target}", possible)
            return possible
        
        return helper(target, candidates)
