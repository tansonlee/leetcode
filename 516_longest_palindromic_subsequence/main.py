from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def helper(start, end):
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                return 2 + helper(start + 1, end - 1)
            return max(helper(start + 1, end), helper(start, end - 1))
        
        return helper(0, len(s) - 1)
