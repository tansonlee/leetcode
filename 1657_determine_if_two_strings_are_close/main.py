from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        chars1 = set(word1)
        chars2 = set(word2)

        for c in chars1:
            if c not in chars2:
                return False
        for c in chars2:
            if c not in chars1:
                return False

        c1 = defaultdict(int)
        c2 = defaultdict(int)

        for c in word1:
            c1[c] += 1

        for c in word2:
            c2[c] += 1
        
        count_of_counts1 = defaultdict(int)
        count_of_counts2 = defaultdict(int)

        for cnt in c1:
            count_of_counts1[c1[cnt]] += 1
        for cnt in c2:
            count_of_counts2[c2[cnt]] += 1
        
        for cnt in count_of_counts1:
            if count_of_counts2[cnt] != count_of_counts1[cnt]:
                return False

        for cnt in count_of_counts2:
            if count_of_counts2[cnt] != count_of_counts1[cnt]:
                return False
        
        return True
        


        
