class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 
            
            if grid[row][col] != '1':
                return
            
            grid[row][col] = '0'
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        result = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    result += 1
                    dfs(row, col)
        
        return result
        
