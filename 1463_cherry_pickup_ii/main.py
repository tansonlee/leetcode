from functools import cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [-1, 0, 1]

        @cache
        def helper(curr_row, pos1, pos2):
            if curr_row == rows or pos1 < 0 or pos1 >= cols or pos2 < 0 or pos2 >= cols:
                return 0 
            
            result = 0
            for dc1 in directions:
                for dc2 in directions:
                    result = max(result, helper(curr_row + 1, pos1 + dc1, pos2 + dc2))
            
            if pos1 == pos2:
                return result + grid[curr_row][pos1]
            else:
                return result + grid[curr_row][pos1] + grid[curr_row][pos2]
            
        return helper(0, 0, cols - 1)
        
