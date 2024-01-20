class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[float("inf") for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        neighbors = [(-1, -1), (-1, 0), (-1, 1)]

        for i in range(len(matrix[0])):
            dp[0][i] = matrix[0][i]
        
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
                for dr, dc in neighbors:
                    r = row + dr
                    c = col + dc
                    if c >= 0 and c < len(matrix[0]):
                        dp[row][col] = min(dp[row][col], dp[r][c] + matrix[row][col])
        
        return min(dp[-1])
        
