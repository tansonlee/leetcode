class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [dist[i] / speed[i] for i in range(len(dist))]

        times.sort()
        for i in range(len(times)):
            if times[i] <= i:
                return i
        
        return len(times)
