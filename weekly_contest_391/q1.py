class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = 0
        for c in str(x):
            s += int(c)
        if x % s == 0:
            return s
        return -1


s = Solution()
print(s.sumOfTheDigitsOfHarshadNumber(18))
print(s.sumOfTheDigitsOfHarshadNumber(23))