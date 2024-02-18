from functools import cache
from collections import defaultdict
import math

class Solution:
    def mostFrequentPrime(self, mat):
        num_rows = len(mat)
        num_cols = len(mat[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def is_prime(n):
            if n < 10:
                return False
            for i in range(2, math.floor(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        @cache
        def primes(row, col, direction):
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return []

            dr, dc = direction
            next_row = row + dr
            next_col = col + dc
            future = primes(next_row, next_col, direction)
            
            result = [mat[row][col]]
            for p in future:
                result.append(int(str(mat[row][col]) + str(p)))
            return result
        
        # print(primes(0, 0, (0, 1)))
        
        counts = defaultdict(int)
        for row in range(num_rows):
            for col in range(num_cols):
                for d in directions:
                    ps = primes(row, col, d)
                    for p in ps:
                        if is_prime(p):
                            counts[p] += 1

        result = None
        for p in counts:
            if result == None:
                result = p
            elif counts[p] > counts[result]:
                result = p
            elif counts[p] == counts[result] and p > result:
                result = p
        return result if result is not None else -1

        
