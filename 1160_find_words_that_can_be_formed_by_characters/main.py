class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counts = {}
        for c in chars:
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
        
        result = 0
        for word in words:
            d = counts.copy()
            is_valid = True
            for c in word:
                if c not in d or d[c] == 0:
                    is_valid = False
                    break
                d[c] -= 1
            if is_valid:
                result += len(word)
        
        return result

            
