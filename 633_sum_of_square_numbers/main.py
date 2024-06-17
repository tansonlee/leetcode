class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0, ceil(sqrt(2 ** 31))):
            b_squared = c - a ** 2
            if b_squared < 0:
                break
            if math.sqrt(b_squared).is_integer():
                return True
        return False

        
