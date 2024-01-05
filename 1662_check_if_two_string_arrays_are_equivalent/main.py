class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = 0
        i2 = 0
        c1 = 0
        c2 = 0
        while i1 < len(word1) and i2 < len(word2):
            print(i1, i2, c1, c2, word1[i1][c1], word2[i2][c2])
            if word1[i1][c1] != word2[i2][c2]:
                return False
            
            c1 += 1
            c2 += 1

            if c1 == len(word1[i1]):
                c1 = 0
                i1 += 1
            if c2 == len(word2[i2]):
                c2 = 0
                i2 += 1


        if i1 != len(word1) or i2 != len(word2):
            return False
        
        return True
        
