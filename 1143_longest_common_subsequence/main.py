from functools import cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def helper(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)
            return max(helper(i, j + 1), helper(i + 1, j))

        return helper(0, 0)

        # dp[i][j] = LCS for text1[0:i+1] and text2[0:j+1]
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        for i in range(len(text1)):
            dp[i][0] = 1 if text2[0] in text1[:i + 1] else 0

        for i in range(len(text2)):
            dp[0][i] = 1 if text1[0] in text2[:i + 1] else 0

        # dp[i][j] = max(dp[i-1][j], dp[i][j-1], if text1[i] == text2[j] dp[i-1][j-1])
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[len(text1) - 1][len(text2) - 1]

