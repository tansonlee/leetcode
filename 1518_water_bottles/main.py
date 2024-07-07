class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        extras = 0
        while (numBottles + extras) >= numExchange:
            numBottles, extras = (numBottles + extras) // numExchange, (numBottles + extras) % numExchange
            result += numBottles
        return result

        
