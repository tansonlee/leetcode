class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [x for x, _ in points]
        points.sort()
        result = 0
        for i in range(len(points) - 1):
            result = max(result, points[i + 1] - points[i])
        return result
