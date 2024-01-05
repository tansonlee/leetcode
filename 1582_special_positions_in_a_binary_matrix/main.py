class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_ones = [0 for _ in range(len(mat))]
        col_ones = [0 for _ in range(len(mat[0]))]

        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1:
                    row_ones[row] += 1
                    col_ones[col] += 1

        result = 0
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == 1 and row_ones[row] == 1 and col_ones[col] == 1:
                    result += 1
        
        return result

