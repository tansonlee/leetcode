class Solution:

    def __init__(self, w: List[int]):
        self.cumulative = [0]
        for i in range(len(w)):
            self.cumulative.append(self.cumulative[-1] + w[i])
        self.total = self.cumulative[-1]

    def pickIndex(self) -> int:
        rand = random.randint(0, self.total - 1)

        # Find the index such that c[i] <= rand < c[i + 1]
        left = 0
        right = len(self.cumulative) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.cumulative[mid] <= rand and rand < self.cumulative[mid + 1]:
                return mid
            if self.cumulative[mid] < rand:
                left = mid + 1
            else:
                right = mid - 1
        




        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
