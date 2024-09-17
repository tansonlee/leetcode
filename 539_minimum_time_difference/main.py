class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def get_mins(time):
            hours, mins = time.split(":")
            return int(hours) * 60 + int(mins)
        
        timePoints = [(get_mins(x), x) for x in timePoints]
        timePoints.sort()

        result = inf
        for i in range(len(timePoints) - 1):
            result = min(result, timePoints[i + 1][0] - timePoints[i][0])
        
        # First and last.
        if len(timePoints) > 1:
            result = min(result, timePoints[0][0] + 1440 - timePoints[-1][0])

        return result

        
