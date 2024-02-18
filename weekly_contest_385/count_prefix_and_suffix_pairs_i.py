class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(w1, w2):
            return w2[:len(w1)] == w1 and w2[-len(w1):] == w1

        result = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        return result
