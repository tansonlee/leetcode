class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        for col in range(n):
            for row in range(1, m):
                if matrix[row][col] != 0:
                    matrix[row][col] = matrix[row - 1][col] + 1

        result = 0
        for row in range(m):
            matrix[row].sort(reverse=True)
            for col in range(n):
                result = max(result, matrix[row][col] * (col + 1))

        return result

