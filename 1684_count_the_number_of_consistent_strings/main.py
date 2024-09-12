class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        def is_consistent(word):
            for c in word:
                if c not in allowed:
                    return False
            return True

        result = 0
        for word in words:
            if is_consistent(word):
                result += 1
        return result


        
