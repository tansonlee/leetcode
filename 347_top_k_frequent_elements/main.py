import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        heap = []
        for n in counts:
            heappush(heap, (counts[n], n))
            if len(heap) > k:
                heappop(heap)
        return [x[1] for x in heap]

