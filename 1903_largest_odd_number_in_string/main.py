class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if num[i] in '13579':
                return num[:i + 1]
        
        return ""

        
