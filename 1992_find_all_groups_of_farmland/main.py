class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []

        for row in range(len(land)):
            for col in range(len(land[row])):
                if land[row][col] == 1:
                    width = 1
                    height = 1
                    while row + height < len(land) and land[row + height][col] == 1:
                        height += 1

                    while True:
                        finished = False
                        for dh in range(height):
                            if col + width - 1 >= len(land[0]) or land[row + dh][col + width - 1] == 0:
                                finished = True
                                break
                        if finished:
                            break
                        for dh in range(height):
                            land[row + dh][col + width - 1] = 0
                        width += 1
                    
                    result.append([row, col, row + height - 1, col + width - 2])
        
        return result

        
