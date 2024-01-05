class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
        
        for char in t:
            if char not in d:
                return False
            if d[char] == 0:
                return False
            d[char] -= 1
        
        for k in d:
            if d[k] != 0:
                return False
        
        return True
            

        
