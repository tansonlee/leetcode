from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        all_valid = True
        for c in counts:
            if counts[c] < k:
                all_valid = False
        if all_valid:
            return len(s)
        
        result = 0
        curr = ""
        for c in s:
            if counts[c] < k:
                result = max(result, self.longestSubstring(curr, k))
                curr = ""
            else:
                curr += c
        if len(curr):
            result = max(result, self.longestSubstring(curr, k))
        return result

