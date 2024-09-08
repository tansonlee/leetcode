from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        self.nums = SortedList()
        

    def addNum(self, value: int) -> None:
        self.nums.add(value)
        

    def getIntervals(self) -> List[List[int]]:
        result = []
        for num in self.nums:
            if len(result) == 0 or num > result[-1][-1] + 1:
                result.append([num, num])
            elif result[-1][-1] + 1 == num:
                result[-1][-1] += 1
        return result

        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
