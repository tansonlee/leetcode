class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result = 0
        open_count = 0

        for c in s:
            if c == '(':
                open_count += 1
            else:
                if open_count == 0:
                    result += 1
                else:
                    open_count -= 1
        result += open_count
        return result


        
