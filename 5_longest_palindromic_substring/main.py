class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Runtime: O(n^2)
        # Space: O(1)
        result = ""

        for i in range(len(s)):
            # Expand from character
            left = i
            right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1

            # Expand from between current and next character
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left:right+1]
                left -= 1
                right += 1
        
        return result

        # Runtime: O(n^2)
        # Space: O(n^2)
        dp = [[0] * len(s) for i in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
            if i < len(s) - 1 and s[i] == s[i+1]:
                dp[i][i+1] = 1

        for i in reversed(range(0, len(s) - 1)):
            for j in range(i + 2, len(s)):
                dp[i][j] = 1 if dp[i+1][j-1] and s[i] == s[j] else 0

        result = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] and j - i + 1 > len(result):
                    result = s[i:j+1]
        return result


