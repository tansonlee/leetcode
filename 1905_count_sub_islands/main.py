class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark all the cells of the island starting from row, col
        # as a 0 in grid2. Return whether this island is a sub island.
        def dfs(row, col):
            stack = [(row, col)]

            result = True

            while stack:
                r, c = stack.pop()
                if r < 0 or r >= len(grid1) or c < 0 or c >= len(grid1[r]):
                    continue
                
                if grid2[r][c] == 0:
                    continue

                grid2[r][c] = 0

                if grid1[r][c] == 0:
                    result = False
                
                for dr, dc in neighbors:
                    stack.append((r + dr, c + dc))
            
            return result

        result = 0

        for row in range(len(grid1)):
            for col in range(len(grid1[row])):
                if grid2[row][col] == 1:
                    result += dfs(row, col)

        return result
        
