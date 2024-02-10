from functools import cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        @cache
        def is_palindrome(s):
            return s == s[::-1]
        
        @cache
        def helper(s):
            if len(s) == 0:
                return [[]]
            result = []
            for i in range(len(s)):
                if is_palindrome(s[:i + 1]):
                    rest = helper(s[i + 1:])
                    for ans in rest:
                        result.append([s[:i + 1]] + ans)
            return result
        
        return helper(s)

