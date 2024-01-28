from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        cumulative = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        c = 0
        for row in range(len(matrix)):
            c += matrix[row][0]
            cumulative[row][0] = c

        c = 0
        for col in range(len(matrix[0])):
            c += matrix[0][col]
            cumulative[0][col] = c

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                cumulative[row][col] = matrix[row][col] + cumulative[row][col - 1] + cumulative[row - 1][col] - cumulative[row - 1][col - 1]
        
        def get_cumulative(row, col):
            if row < 0 or col < 0:
                return 0
            return cumulative[row][col]

        def submatrix_sum(r1, c1, r2, c2):
            return get_cumulative(r2, c2) - get_cumulative(r2, c1 - 1) - get_cumulative(r1 - 1, c2) + get_cumulative(r1 - 1, c1 - 1)

        result = 0
        for row1 in range(len(matrix)):
            for row2 in range(row1, len(matrix)):
                counts = defaultdict(int)
                counts[0] = 1
                for c in range(len(matrix[0])):
                    s = submatrix_sum(row1, 0, row2, c)
                    if (s - target) in counts:
                        result += counts[s - target]
                    counts[s] += 1
                    
        return result
        
