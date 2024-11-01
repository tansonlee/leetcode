class Solution:
    def makeFancyString(self, s: str) -> str:
        prev_count = 0
        result = "0"
        for char in s:
            if char == result[-1]:
                if prev_count < 2:
                    prev_count += 1
                    result += char
            else:
                prev_count = 1
                result += char
        
        return result[1:]
        
