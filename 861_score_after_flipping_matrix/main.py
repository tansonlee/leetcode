class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def flip_row(row):
            for col in range(len(grid[row])):
                grid[row][col] = abs(grid[row][col] - 1)
        
        def flip_col(col):
            for row in range(len(grid)):
                grid[row][col] = abs(grid[row][col] - 1)

        for row in range(len(grid)):
            if grid[row][0] == 0:
                flip_row(row)
        print(grid)
        for col in range(len(grid[0])):
            count = 0
            for row in range(len(grid)):
                if grid[row][col]:
                    count += 1
            if count < len(grid) / 2:
                flip_col(col)
        
        result = 0
        for row in grid:
            for i in range(len(row)):
                result += (2 ** (len(row) - i - 1)) * row[i]
                print(result)

        print(grid)
        return result
        
