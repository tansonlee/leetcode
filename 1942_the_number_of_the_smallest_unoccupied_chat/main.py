class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        unoccupied = [i for i in range(len(times))]
        heapify(unoccupied)

        events = [(times[i][0], times[i][1], i) for i in range(len(times))]
        events.sort()

        leaves = []

        for arrive, leave, num in events:
            while leaves and leaves[0][0] <= arrive:
                _, spot = heappop(leaves)
                heappush(unoccupied, spot)
            
            if num == targetFriend:
                return unoccupied[0]
            
            spot = heappop(unoccupied)
            heappush(leaves, (leave, spot))
        


