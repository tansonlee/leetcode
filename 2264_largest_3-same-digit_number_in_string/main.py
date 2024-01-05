class Solution:
    def largestGoodInteger(self, num: str) -> str:
        s = ""
        for i in range(len(num) - 2):
            a = num[i]
            b = num[i + 1]
            c = num[i + 2]

            if a == b and b == c:
                if s == "" or int(num[i:i+3]) > int(s):
                    s = num[i:i+3]
        
        return s

        
