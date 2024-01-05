from functools import cache

class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        print("callingon", s)
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        result = self.numDecodings(s[1:])
        if s[0] == "1":
            result += self.numDecodings(s[2:])
        elif s[0] == "2" and s[1] in "0123456":
            result += self.numDecodings(s[2:])
        return result
