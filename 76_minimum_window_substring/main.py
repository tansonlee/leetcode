from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        c = len(t) # count of all positive keys in d

        for char in t:
            d[char] += 1
        
        start = 0
        end = 0
        result = [float("inf"), ""]

        while start < len(s):
            # contract 
            if end >= len(s) or c == 0:
                if s[start] in d:
                    d[s[start]] += 1
                    if d[s[start]] > 0:
                        c += 1
                start += 1
            # expand 
            else:
                if s[end] in d:
                    d[s[end]] -= 1
                    if d[s[end]] >= 0:
                        c -= 1
                end += 1
            if c == 0 and end - start + 1 < result[0]:
                result = [end - start + 1, s[start: end]]

        return result[1]

