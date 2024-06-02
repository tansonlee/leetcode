class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def is_valid(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row])

        directions = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2)]

        queue = deque([(0, 0, 1)])
        visited = set()

        while queue:
            row, col, cost = queue.popleft()
            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return cost
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if not is_valid(new_row, new_col):
                    continue
                if grid[new_row][new_col] == 1:
                    continue
                
                queue.append((new_row, new_col, cost + 1))
        
        return -1


        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        def is_valid(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row])

        directions = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2)]
        
        heap = [(1, 0, 0)]
        visited = set()
        while heap:
            cost, row, col = heappop(heap)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            if row == len(grid) - 1 and col == len(grid[row]) - 1:
                return cost

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if not is_valid(new_row, new_col):
                    continue
    
                if grid[new_row][new_col] == 1:
                    continue
                
                heappush(heap, (cost + 1, new_row, new_col))

        return -1
            

            

