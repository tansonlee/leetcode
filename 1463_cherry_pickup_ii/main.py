from functools import cache

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [-1, 0, 1]

        #####
        # Bottom up approach
        #####
        # dp[row][p1][p2] = best you can do up to row where robots end at p1 and p2
        dp = [[[float("-inf") for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

        dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]
        
        for row in range(1, rows):
            for c1 in range(cols):
                for c2 in range(cols):
                    # Each of c1 and c2 could have been arrived at by up to 3 places
                    for dc1 in directions:
                        for dc2 in directions:
                            from_c1 = c1 + dc1
                            from_c2 = c2 + dc2
                            if from_c1 < 0 or from_c1 >= cols or from_c2 < 0 or from_c2 >= cols:
                                continue
                            dp[row][c1][c2] = max(dp[row][c1][c2], dp[row - 1][from_c1][from_c2])
                    if c1 != c2:
                        dp[row][c1][c2] += grid[row][c1] + grid[row][c2]
                    else:
                        dp[row][c1][c2] += grid[row][c1]

        return max([max(x) for x in dp[-1]])


        #####
        # Top down approach
        #####
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
        
