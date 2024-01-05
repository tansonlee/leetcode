class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        result = [[0 for _ in range(len(img[0]))] for _ in range(len(img))]

        dirs = [(1, 0),
                (1, 1),
                (1, -1),
                (-1, 0),
                (-1, 1),
                (-1, -1),
                (0, 0),
                (0, 1),
                (0, -1) ]
        for row in range(len(img)):
            for col in range(len(img[row])):
                possibles = []
                for dr, dc in dirs:
                    possibles.append((row + dr, col + dc))

                total = 0
                cnt = 0
                for r, c in possibles:
                    if r < 0 or c < 0 or r >= len(img) or c >= len(img[0]):
                        continue
                    cnt += 1
                    total += img[r][c]
                result[row][col] = total // cnt
        
        return result
                
                


                
