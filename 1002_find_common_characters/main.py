class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def intersection(l1, l2):
            count1 = Counter(l1)
            count2 = Counter(l2)

            result = []
            for c in count1:
                if c in count2:
                    result.extend([c for _ in range(min(count1[c], count2[c]))])
            return result

        result = list(words[0])

        for w in words:
            result = intersection(result, list(w))

        return result

