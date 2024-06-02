class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heappush(heap, (-(x * x + y * y) ,x,y))
            if len(heap) > k:
                heappop(heap)
        return [[x, y] for _, x, y in heap]
            



