class Solution:
    def myPow(self, x: float, n: int) -> float:
        abs_n = abs(n)

        result = None
        if abs_n == 0:
            result = 1
        elif abs_n == 1:
            result = x
        else:
            half = self.myPow(x, abs_n // 2)
            result = half * half * (x if abs_n % 2 == 1 else 1)

        if n < 0:
            return 1 / result
        else:
            return result
        

            


        
