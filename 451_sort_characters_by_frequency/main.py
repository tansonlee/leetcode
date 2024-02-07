from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        count_and_char = [(counts[char], char) for char in counts]
        count_and_char.sort(reverse=True)

        result = ""
        for count, char in count_and_char:
            for _ in range(count):
                result += char
        
        return result

        
