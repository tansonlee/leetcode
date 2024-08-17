class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(points[0]))] for _ in range(len(points))]
        for col in range(len(points[0])):
            dp[0][col] = points[0][col]
        
        for row in range(1, len(points)):
            # Precompute
            left = [0 for _ in range(len(points[row]))]
            right = [0 for _ in range(len(points[row]))]
            left[0] = dp[row - 1][0]
            right[-1] = dp[row - 1][-1]

            for col in range(1, len(points[row])):
                left[col] = max(left[col - 1] - 1, dp[row - 1][col])
            
            for col in reversed(range(len(points[row]) - 1)):
                right[col] = max(right[col + 1] - 1, dp[row - 1][col])

            for col in range(len(points[row])):
                dp[row][col] = max(left[col], right[col]) + points[row][col]
        
        return max(dp[-1])

        
