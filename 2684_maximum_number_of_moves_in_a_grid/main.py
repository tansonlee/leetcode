class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        dp = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for row in range(len(grid)):
            dp[row][0] = 0
        
        for col in range(1, len(grid[0])):
            for row in range(len(grid)):
                for dr in range(-1, 2):
                    other_col = col - 1
                    other_row = row + dr
                    if other_row < 0 or other_row >= len(grid):
                        continue
                    
                    if grid[other_row][other_col] >= grid[row][col]:
                        continue
                    
                    if dp[other_row][other_col] == -1:
                        continue

                    dp[row][col] = max(dp[row][col], dp[other_row][other_col] + 1)
        
        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                result = max(result, dp[row][col])
        
        return result


        
