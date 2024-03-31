class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = numBottles
        result = numBottles
        numBottles = 0
        
        while emptyBottles >= numExchange:
            emptyBottles -= numExchange
            result += 1
            emptyBottles += 1
            numExchange += 1
        return result


s = Solution()
print(s.maxBottlesDrunk(13, 6))
print(s.maxBottlesDrunk(10, 3))