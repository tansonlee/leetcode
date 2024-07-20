class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        for row in range(len(rowSum)):
            result[row][0] = rowSum[row]
        
        for col in range(len(colSum) - 1):
            curr_col_sum = 0
            for row in range(len(rowSum)):
                curr_col_sum += result[row][col]
                
            remaining = curr_col_sum - colSum[col]
            for row in range(len(rowSum)):
                if remaining == 0:
                    break
                bring_over = min(remaining, result[row][col])
                result[row][col + 1] += bring_over
                result[row][col] -= bring_over
                remaining -= bring_over
        
        return result


        
