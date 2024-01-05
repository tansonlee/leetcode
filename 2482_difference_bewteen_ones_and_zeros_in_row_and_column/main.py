class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones_row = [0 for _ in range(len(grid))]
        zeros_row = [0 for _ in range(len(grid))]

        ones_col = [0 for _ in range(len(grid[0]))]
        zeros_col = [0 for _ in range(len(grid[0]))]

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    ones_row[row] += 1
                    ones_col[col] += 1
                else:
                    zeros_row[row] += 1
                    zeros_col[col] += 1
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                grid[row][col] = ones_row[row] + ones_col[col] - zeros_row[row] - zeros_col[col]
        
        return grid

        
