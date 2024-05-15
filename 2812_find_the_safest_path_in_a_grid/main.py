class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        safety = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def valid_pos(row, col):
            return not (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]))

        def calculate_safety(sources):
            q = deque(sources)
            visited = set()
            while q:
                row, col, val = q.popleft()
                visited.add((row, col))
                if safety[row][col] != 0:
                    safety[row][col] = val
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if not valid_pos(new_row, new_col):
                        continue
                    if (new_row, new_col) in visited:
                        continue
                    visited.add((new_row, new_col))
                    q.append((new_row, new_col, val + 1))

        sources = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    safety[row][col] = 0
                    sources.append((row, col, 0))
            
        calculate_safety(sources)
        print(safety)

        # can do within safeness factor
        @cache
        def can(safeness):
            q = deque([(0, 0)])
            visited = set()
            while q:
                row, col = q.popleft()
                if not valid_pos(row, col):
                    continue
                if safety[row][col] < safeness:
                    continue
                if (row, col) in visited:
                    continue
                visited.add((row, col))

                if row == len(grid) - 1 and col == len(grid[row]) - 1:
                    return True
                
                for dr, dc in directions:
                    q.append((row + dr, col + dc))
            return False

        # binary search for answer
        low = 0
        high = 0 # len(grid) + len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                high = max(high, safety[row][col])
        
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if can(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1

        return result
        

        
