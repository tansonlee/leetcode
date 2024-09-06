class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counts = Counter(words)

        result = 0
        used_middle = False
        for word in counts:
            if word[0] == word[1]:
                count = counts[word]
                if not used_middle:
                    result += count * 2
                    if count % 2 == 1:
                        used_middle = True
                else:
                    result += (count // 2 * 2) * 2
            else:
                forward_count = counts[word]
                backward_count = counts[word[::-1]]
                result += min(forward_count, backward_count) * 2
        
        return result

        
