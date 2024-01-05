from collections import deque

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([(0, 0)])
        result = []
        visited = set()

        while q:
            row, col = q.popleft()
            if (row, col) in visited:
                continue
            result.append(nums[row][col])
            visited.add((row, col))

            candidate1 = (row + 1, col)
            candidate2 = (row, col + 1)

            if candidate1[0] < len(nums) and candidate1[1] < len(nums[candidate1[0]]) and candidate1 not in visited:
                q.append(candidate1)

            if candidate2[0] < len(nums) and candidate2[1] < len(nums[candidate2[0]]) and candidate2 not in visited:
                q.append(candidate2)

        return result



        # result = []
        # for i in range(len(nums)):
        #     for j in range(len(nums[i])):
        #         result.append((i, i + j, nums[i][j]))
        # result.reverse()
        # result.sort(key=lambda x : x[1])
        # result = [x[2] for x in result]

        # return result

        # result = []
        # # First do the rows
        # for i in range(len(nums)):
        #     row = i
        #     col = 0
        #     while row >= 0:
        #         if col < len(nums[row]):
        #             result.append(nums[row][col])
        #         row -= 1
        #         col += 1
        
        # col_iterations = max([len(x) - len(nums) + i for i,x in enumerate(nums)])
        # for i in range(col_iterations):
        #     row = len(nums) - 1
        #     col = i + 1
        #     while row >= 0:
        #         if col < len(nums[row]):
        #             result.append(nums[row][col])
        #         row -= 1
        #         col += 1
        # return result
                
        
