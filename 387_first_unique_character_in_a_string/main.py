from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = defaultdict(int)

        for char in s:
            c[char] += 1
        
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        
        return -1
        
