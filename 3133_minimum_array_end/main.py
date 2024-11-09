class Solution:
    def minEnd(self, n: int, x: int) -> int:
        result = 0
        curr_in_n = 0
        n = n - 1 # Dumb why the question does this

        for bit in range(64):
            if (x >> bit) & 1:
                result = result | (2 ** bit)
            else:
                if (n >> curr_in_n) & 1:
                    result = result | (2 ** bit)
                curr_in_n += 1
        
        return result

        
