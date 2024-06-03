class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.values = deque([])
        self.sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        if self.count >= self.size:
            old = self.values.popleft()
            self.sum -= old
            self.count -= 1
        
        self.sum += val
        self.count += 1
        self.values.append(val)
        return self.sum / self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
