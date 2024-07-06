class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        full_rounds = time // (n - 1) 
        offset = time % (n - 1)
        if full_rounds % 2 == 0:
            return offset + 1
        else:
            return n - offset
        
