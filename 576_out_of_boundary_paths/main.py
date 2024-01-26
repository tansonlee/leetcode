from functools import cache

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def helper(row, col, moves):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            if moves == 0:
                return 0
            
            result = 0
            for dr, dc in dirs:
                result += helper(row + dr, col + dc, moves - 1)
            return result
        
        return helper(startRow, startColumn, maxMove) % (10 ** 9 + 7)

            

