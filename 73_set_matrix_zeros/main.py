class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Check if the first row should be filled completely
        first_row = False
        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                first_row = True
                break
        
        # Check if the first col should be filled completely
        first_col = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                first_col = True
                break

        # Use the first row/col to provide lookup for where zeros are
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        # Use the lookup we just setup to modify the matrix in place
        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[row])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Fill out the first row if necessary
        if first_row:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        
        # Fill out the first col if necessary
        if first_col:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        
