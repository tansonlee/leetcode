class Leaderboard:

    def __init__(self):
        self.scores = {}
        

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0
        
        self.scores[playerId] += score
        

    def top(self, K: int) -> int:
        # use a heap to find the top K
        heap = []

        for playerId in self.scores:
            score = self.scores[playerId]
            if len(heap) < K:
                heappush(heap, score)
            elif score > heap[0]:
                heappop(heap)
                heappush(heap, score)
        return sum(heap)


    def reset(self, playerId: int) -> None:
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
