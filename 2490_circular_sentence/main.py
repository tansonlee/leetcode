class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        for i in range(len(words) - 1):
            curr_word = words[i]
            next_word = words[i + 1]

            if curr_word[-1] != next_word[0]:
                return False
        
        if words[0][0] != words[-1][-1]:
            return False
            
        return True
        
