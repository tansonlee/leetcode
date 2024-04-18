class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def invalid(i, j):
            return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                
                for di, dj in directions:
                    newi = i + di
                    newj = j + dj
                    if invalid(newi, newj):
                        res += 1
                    elif grid[newi][newj] == 0:
                        res += 1
        
        return res
                

                
        
