class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for k in range(n//2):
            for i in range(n - 1 - (2*k)):
                p1 = (k, i+k)
                p2 = (i+k, n-1-k)
                p3 = (n-1-k, n-1-i-k)
                p4 = (n-1-i-k, k)

                v1 = matrix[p1[0]][p1[1]]
                v2 = matrix[p2[0]][p2[1]]
                v3 = matrix[p3[0]][p3[1]]
                v4 = matrix[p4[0]][p4[1]]

                matrix[p2[0]][p2[1]] = v1
                matrix[p3[0]][p3[1]] = v2
                matrix[p4[0]][p4[1]] = v3
                matrix[p1[0]][p1[1]] = v4
        
