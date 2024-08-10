class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # Idea: create a graph to represent the board
        # graph needs 3x the size of the initial grid to differentiate \ and /
        # Maybe could do 2 technically but 3 is easier to reason about.
        n = len(grid) * 3
        graph = [[0 for _ in range(n)] for _ in range(n)]

        def handle_fill(row, col, char):
            if char == ' ':
                return
            
            rrow = row * 3
            rcol = col * 3

            graph[rrow + 1][rcol + 1] = 1

            if char == '\\':
                graph[rrow][rcol] = 1
                graph[rrow + 2][rcol + 2] = 1
            if char == '/':
                graph[rrow + 2][rcol] = 1
                graph[rrow][rcol + 2] = 1
            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                handle_fill(row, col, grid[row][col])
        
        def flood_fill(row, col):
            if row < 0 or row >= len(graph) or col < 0 or col >= len(graph):
                return
            if graph[row][col] == 1:
                return
            
            graph[row][col] = 1
            flood_fill(row + 1, col)
            flood_fill(row - 1, col)
            flood_fill(row, col + 1)
            flood_fill(row, col - 1)
        
        result = 0
        for row in range(len(graph)):
            for col in range(len(graph)):
                if graph[row][col] == 0:
                    result += 1
                    flood_fill(row, col)

        return result
        
