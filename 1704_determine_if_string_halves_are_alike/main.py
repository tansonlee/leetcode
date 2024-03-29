class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        first = 0
        second = 0

        for i in range(len(s) // 2):
            if s[i] in vowels:
                first += 1
        
        for i in range(len(s) // 2, len(s)):
            if s[i] in vowels:
                second += 1
        
        return first == second
        
