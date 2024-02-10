class Solution:
    def countSubstrings(self, s: str) -> int:
        #####
        # Expand outwards from every source
        #####
        result = 0

        # Odd length
        for source in range(len(s)):
            spread = 0
            while source - spread >= 0 and source + spread < len(s):
                if s[source - spread] == s[source + spread]:
                    result += 1
                else:
                    break
                spread += 1

        # Even length
        for source in range(1, len(s)):
            left = source - 1
            right = source
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    result += 1
                else:
                    break
                left -= 1
                right += 1
        
        return result


        #####
        # Bottom up dp
        #####
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # A single character is always a palindrome.
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in reversed(range(len(s) - 1)):
            for j in range(i, len(s)):
                if s[i] != s[j]:
                    continue

                if j - i == 1: # Next to each other
                    dp[i][j] = 1
                elif dp[i + 1][j - 1]:
                    dp[i][j] = 1 

        return sum([sum(x) for x in dp])

