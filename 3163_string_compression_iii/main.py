class Solution:
    def compressedString(self, word: str) -> str:
        result = ""

        idx = 0
        while idx < len(word):
            char = word[idx]
            count = 0

            for _ in range(min(9, len(word) - idx)):
                if word[idx] == char:
                    count += 1
                else:
                    break
                
                idx += 1
            
            result += f"{count}{char}"
        
        return result
        
