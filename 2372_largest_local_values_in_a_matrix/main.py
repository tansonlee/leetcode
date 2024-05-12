class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0 for _ in range(n - 2)] for _ in range(n - 2)]
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

        for i in range(n - 2):
            for j in range(n - 2):
                cr, cc = i + 1, j + 1
                local_max = -1
                for dr, dc in neighbors:
                    local_max = max(local_max, grid[cr + dr][cc + dc])
                result[i][j] = local_max
        return result

