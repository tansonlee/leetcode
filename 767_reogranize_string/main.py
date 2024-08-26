class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        counts_heap = [(-counts[n], n) for n in counts]
        heapify(counts_heap)

        if counts_heap[0][0] * -1 > ceil(len(s) / 2):
            return "" # Impossible

        result = ["#"]

        while len(counts_heap):
            count = None
            next_letter = None
            if counts_heap[0][1] != result[-1]:
                next_letter = counts_heap[0][1]
                count, next_letter = heappop(counts_heap)
            else:
                top = heappop(counts_heap)
                next_letter = counts_heap[0][1]
                count, next_letter = heappop(counts_heap)
                heappush(counts_heap, top)

            count += 1 # Since we store them as negative b/c min heap
            if count != 0:
                heappush(counts_heap, (count, next_letter))
            
            result.append(next_letter)
            
        return "".join(result[1:])
        
