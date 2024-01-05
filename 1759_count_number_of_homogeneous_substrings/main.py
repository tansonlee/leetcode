class Solution:
    def countHomogenous(self, s: str) -> int:
        def helper(n):
            return (n * (n + 1)) // 2
        
        res = 0
        ptr = 0
        while ptr < len(s):
            curr_char = s[ptr]
            cnt = 0
            while ptr < len(s) and s[ptr] == curr_char:
                ptr += 1
                cnt += 1
            res += helper(cnt)
        
        return res % (10 ** 9 + 7)
        
        
