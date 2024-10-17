class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}

        def insert_trie(word):
            curr = self.trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['end'] = True
        
        for word in words:
            insert_trie(word)
        
        self.curr_ptrs = []

    def query(self, letter: str) -> bool:
        self.curr_ptrs.append(self.trie)

        indexes_to_remove = set()
        for i in range(len(self.curr_ptrs)):
            if letter not in self.curr_ptrs[i]:
                indexes_to_remove.add(i)
            else:
                self.curr_ptrs[i] = self.curr_ptrs[i][letter]
        
        new_curr_ptrs = []
        for i in range(len(self.curr_ptrs)):
            if i not in indexes_to_remove:
                new_curr_ptrs.append(self.curr_ptrs[i])
        
        self.curr_ptrs = new_curr_ptrs

        for p in self.curr_ptrs:
            if 'end' in p:
                return True
        
        return False

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
