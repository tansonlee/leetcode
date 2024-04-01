class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(filter(lambda x: len(x), s.split(" ")))[-1])
        
