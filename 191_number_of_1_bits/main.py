import math

class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        d = floor(math.log(n, 2))
        result = 0
        while d >= 0 and n > 0:
            if (2 ** d) <= n:
                result += 1
                n -= (2 ** d)
            d -= 1
        return result
        
