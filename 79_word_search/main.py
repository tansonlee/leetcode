class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def valid(r, c):
            return r >= 0 and c >= 0 and r < len(board) and c < len(board[0])

        def exists_from(row, col, i, visited):
            if word[i] != board[row][col]:
                return False

            if (row, col) in visited:
                return False
            visited.add((row, col))

            if i == len(word) - 1:
                return True
            
            for dr, dc in directions:
                new_r = row + dr
                new_c = col + dc
                if not valid(new_r, new_c):
                    continue
                if exists_from(new_r, new_c, i + 1, visited):
                    return True
            visited.remove((row, col))
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                visited = set()
                if exists_from(r, c, 0, visited):
                    return True
        return False
            


