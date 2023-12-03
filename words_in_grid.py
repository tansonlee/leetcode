# Given a list of valid words and a grid of characters, determine which words are in the grid.
class Trie:
    def __init__(self):
        self.root = TrieNode(True, {})
    
    def insert(self, string):
        current = self.root

        for char in string:
            if char not in current.children:
                current.children[char] = TrieNode(False, {})
            current = current.children[char]
        current.is_leaf = True

class TrieNode:
    def __init__(self, is_leaf, children):
        self.is_leaf = is_leaf
        self.children = children
    
    def __repr__(self) -> str:
        new = self.children.copy()
        new["aa_is_leaf"] = 1 if self.is_leaf else 0
        return f"{new}"
        
        
    def __str__(self) -> str:
        new = self.children.copy()
        new["aa_is_leaf"] = 1 if self.is_leaf else 0
        return f"{new}"

# O(words * len(max_len_word))
def next_char(words, substring):
    result = []
    for word in words:
        if word[0:len(substring)] == substring:
            if len(substring) < len(word):
                result.append(word[len(substring)])
    return result

# perform a dfs starting at row, col
def dfs(grid, words, trie, r, c):
    dbg = r == 0 and c == 0 and True
    if dbg:
        print(trie.children, grid[r][c])
    if grid[r][c] not in trie.children:
        return []
    stack = [[r, c, "", trie.children[grid[r][c]]]]
    result = []

    while len(stack):
        row, col, substring, trie = stack.pop()
        # substring is the substring up until now.
        substring = substring + grid[row][col]
        if dbg:
            print(row, col, substring)

        if trie.is_leaf:
            print("adding", substring)
            result.append(substring)
        # if substring in words:
        #     result.append(substring)

        # get possible next characters to visit.
        next_chars = list(trie.children.keys())
        next_chars2 = next_char(words, substring)
        if dbg:
            print("next chars", next_chars,next_chars2)

        # add neighbors into stack
        # row, col - 1
        
        if col - 1 >= 0 and grid[row][col - 1] in next_chars:
            stack.append([row, col - 1, substring, trie.children[grid[row][col-1]]])
        # row, col + 1
        if col + 1 < len(grid) and grid[row][col + 1] in next_chars:
            stack.append([row, col + 1, substring, trie.children[grid[row][col + 1]]])
        # row + 1, col
        if row + 1 < len(grid) and grid[row + 1][col] in next_chars:
            stack.append([row + 1, col, substring, trie.children[grid[row + 1][col]]])
        # row - 1, col
        if row - 1 >= 0 and grid[row - 1][col] in next_chars:
            stack.append([row - 1, col, substring, trie[grid[row - 1][col]]])

    return result

def solve(words, grid):
    # Start at every point in the grid and perform a dfs for a word.
    results = []

    trie = Trie()
    for w in words:
        trie.insert(w)
    
    print(trie.root)

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            partial_result = dfs(grid, words, trie.root, row, col)
            for r in partial_result:
                results.append(r)
    
    return results

words = ["oath","pea","eat","rain", "eats"]
grid = [
  ['o','a','a','n'],
  ['s','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

print(solve(words, grid))
