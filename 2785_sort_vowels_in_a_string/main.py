class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_counts = [0 for _ in range(10)] # 5 vowels x (lowercase & uppercase)
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

        for char in s:
            if char in vowels:
                pos = vowels.index(char)
                vowel_counts[pos] += 1
        print(vowel_counts)
        
        res = []
        for char in s:
            if char not in vowels:
                res.append(char)
            else:
                next_vowel_index =  -1
                for i in range(len(vowel_counts)):
                    if vowel_counts[i] != 0:
                        next_vowel_index = i
                        vowel_counts[i] -= 1
                        break
                res.append(vowels[next_vowel_index])
        
        return "".join(res)
        
