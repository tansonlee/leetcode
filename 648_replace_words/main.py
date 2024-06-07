class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        class TrieNode:
            def __init__(self, ending):
                self.ending = ending
                self.children = {}
            
            def __repr__(self):
                return f"{self.ending} [{self.children}]"
            
        def insert(node, word):
            curr_node = node
            for c in word:
                if c not in curr_node.children:
                    curr_node.children[c] = TrieNode(False)
                curr_node = curr_node.children[c]
            curr_node.ending = True
        
        def search(node, word):
            curr_node = node
            for i in range(len(word)):
                if curr_node.ending:
                    return word[:i]

                if word[i] not in curr_node.children:
                    return word
                
                curr_node = curr_node.children[word[i]]
            
            return word
        
        trie = TrieNode(False)
        for word in dictionary:
            insert(trie, word)
        
        result = []
        for word in sentence.split(" "):
            found = search(trie, word)
            result.append(found)
        
        return " ".join(result)




        
