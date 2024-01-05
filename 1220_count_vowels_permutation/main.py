class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp[i][j] is the number of strings of length i that ends with the jth vowel
        dp = [[0 for _ in range(5)] for _ in range(n)]

        for i in range(5):
            dp[0][i] = 1
        
        A = 0
        E = 1
        I = 2
        O = 3
        U = 4
        
        for i in range(1,n):
            dp[i][A] = dp[i - 1][E] + dp[i - 1][U] + dp[i - 1][I]
            dp[i][E] = dp[i - 1][A] + dp[i - 1][I]
            dp[i][I] = dp[i - 1][E] + dp[i - 1][O]
            dp[i][O] = dp[i - 1][I]
            dp[i][U] = dp[i - 1][O] + dp[i - 1][I]
        
        return sum(dp[n - 1]) % (10 ** 9 + 7)
        
