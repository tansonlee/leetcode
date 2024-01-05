class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        return money if sorted(prices)[0] + sorted(prices)[1] > money else money - sorted(prices)[0] - sorted(prices)[1]
        
