class Solution:
    def minOperations(self, s: str) -> int:
        way1 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    way1 += 1
            else:
                if s[i] != '1':
                    way1 += 1
        
        way2 = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '1':
                    way2 += 1
            else:
                if s[i] != '0':
                    way2 += 1
        
        return min(way1, way2)
