import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)
        for n in counts:
            buckets[counts[n]].append(n)

        result = []
        for l in reversed(buckets):
            if len(result) == k:
                break
            result.extend(l)
        return result

        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1
        
        heap = []
        for n in counts:
            heappush(heap, (counts[n], n))
            if len(heap) > k:
                heappop(heap)
        return [x[1] for x in heap]

