class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_heights = [0 for _ in range(len(heights))]
        max_heights[-1] = heights[-1]

        for i in reversed(range(len(heights) - 1)):
            max_heights[i] = max(heights[i], max_heights[i+1])
        
        result = []
        for i in range(len(heights) - 1):
            if max_heights[i + 1] < heights[i]:
                result.append(i)
        
        result.append(len(heights) - 1)
        return result

        

