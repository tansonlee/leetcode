class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            result = ""
            for char in s:
                if char == "0":
                    result += "1"
                else:
                    result += "0"
            return result


        @cache
        def create(n):
            if n == 1:
                return "0"
            prev = create(n - 1)
            return prev + "1" + invert(prev)[::-1]
        
        
        string = create(n)
        return string[k - 1]

        
