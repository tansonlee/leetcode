class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can_make_word(word, counts):
            word_counts = defaultdict(int)
            for l in word:
                word_counts[l] += 1
            for l in word_counts:
                if word_counts[l] > counts[l]:
                    return False
            return True
        
        def remove_counts_for_word(word, counts):
            result = counts.copy()
            for l in word:
                result[l] -= 1
            return result
        
        def word_score(word):
            result = 0
            for l in word:
                result += score[ord(l) - ord('a')]
            return result

        letter_counts = defaultdict(int)
        for l in letters:
            letter_counts[l] += 1

        result = 0
        def backtracking(remaining, letter_counts, curr_score):
            nonlocal result
            if len(remaining) == 0:
                result = max(result, curr_score)
                return
            
            backtracking(remaining[1:], letter_counts, curr_score)

            if can_make_word(remaining[0], letter_counts):
                backtracking(remaining[1:], remove_counts_for_word(remaining[0], letter_counts), word_score(remaining[0]) + curr_score)

        backtracking(words, letter_counts, 0)
        return result

            

        
        
