import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = [1]
        self.max_allocated = 1

    def reserve(self) -> int:
        if len(self.seats) > 0:
            return heapq.heappop(self.seats)
        else:
            self.max_allocated += 1
            return self.max_allocated

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seats, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
