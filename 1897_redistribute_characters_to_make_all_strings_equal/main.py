from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        counts = defaultdict(int)

        for word in words:
            for char in word:
                counts[char] += 1
        
        for char in counts:
            if counts[char] % len(words) != 0:
                return False
        
        return True
        
