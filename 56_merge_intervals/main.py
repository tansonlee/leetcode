class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []

        idx = 0
        while idx < len(intervals):
            start = intervals[idx][0]
            end = intervals[idx][1]

            while idx < len(intervals) and intervals[idx][0] <= end:
                end = max(end, intervals[idx][1])
                idx += 1

            result.append([start, end])

        return result
