class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")

        counts1 = Counter(s1)
        counts2 = Counter(s2)

        set1 = set(s1)
        set2 = set(s2)

        result = []
        for x in set1:
            if counts1[x] == 1 and counts2[x] == 0:
                result.append(x)

        for x in set2:
            if counts2[x] == 1 and counts1[x] == 0:
                result.append(x)

        return result
        
