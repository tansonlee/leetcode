class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # Compress the matrices
        mat1_compressed = defaultdict(list) # Given a row, what are the values
        mat2_compressed = defaultdict(list) # Given a col, what are the values

        for row in range(len(mat1)):
            for col in range(len(mat1[row])):
                if mat1[row][col] != 0:
                    mat1_compressed[row].append((col, mat1[row][col]))

        for row in range(len(mat2)):
            for col in range(len(mat2[row])):
                if mat2[row][col] != 0:
                    mat2_compressed[col].append((row, mat2[row][col]))
        
        # Do the multiplication
        result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

        for row in range(len(result)):
            for col in range(len(result[row])):
                mat1_vals = mat1_compressed[row]
                mat2_vals = dict(mat2_compressed[col])

                # Determine the sparse dot product between mat1_vals and mat2_vals
                for a, val in mat1_vals:
                    if a in mat2_vals:
                        result[row][col] += (val * mat2_vals[a])
        
        return result


    def multiply_brute_force(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]

        for row in range(len(result)):
            for col in range(len(result[row])):
                # Go over the row in mat1 and col in mat2
                cell_val = 0
                for i in range(len(mat2)):
                    cell_val += mat1[row][i] * mat2[i][col]

                result[row][col] = cell_val
        
        return result
        
