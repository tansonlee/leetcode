# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        grid = [[-1 for _ in range(n)] for _ in range(m)]

        RIGHT = (0, 1)
        DOWN = (1, 0)
        LEFT = (0, -1)
        UP = (-1, 0)

        pos = (0, 0)
        dir = RIGHT

        def get_next_pos():
            nonlocal pos, dir
            result = pos
            row = pos[0]
            col = pos[1]

            # Calculate the next direction to move
            if dir == RIGHT:
                if col == n - 1 or grid[row][col + 1] != -1:
                    dir = DOWN
            elif dir == DOWN:
                if row == m - 1 or grid[row + 1][col] != -1:
                    dir = LEFT
            elif dir == LEFT:
                if col == 0 or grid[row][col - 1] != -1:
                    dir = UP
            elif dir == UP:
                if row == 0 or grid[row - 1][col] != -1:
                    dir = RIGHT

            pos = (row + dir[0], col + dir[1])

            return result


        curr = head
        while curr:
            row, col = get_next_pos()
            grid[row][col] = curr.val
            curr = curr.next
        
        return grid

