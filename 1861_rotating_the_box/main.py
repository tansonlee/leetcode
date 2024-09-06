class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        result = [['.' for _ in range(len(box))] for _ in range(len(box[0]))]

        # Copy over only the obstacles.
        for row in range(len(box)):
            for col in range(len(box[row])):
                if box[row][col] == '*':
                    result[col][row] = '*'
        
        # Starting from row, col, place stones in the result
        # moving upwards in the column
        def place_stones_from(row, col, count):
            for i in range(count):
                result[row - i][col] = '#'

        # Copy over the fallen stones.
        for row in range(len(box)):
            stone_count = 0
            for col in range(len(box[row])):
                if box[row][col] == '*':
                    # Put the fallen stones into the result
                    if stone_count > 0:
                        # Swap col and row and subtract 1 from col to
                        # get just above the obstacle we are currently on.
                        place_stones_from(col - 1, row, stone_count)
                    stone_count = 0
                elif box[row][col] == '#':
                    stone_count += 1
            if stone_count > 0:
                place_stones_from(len(box[row]) - 1, row, stone_count)
        
        # Need to flip everything horizontally
        for row in result:
            row.reverse()

        return result

        
