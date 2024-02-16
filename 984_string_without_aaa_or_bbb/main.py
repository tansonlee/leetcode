class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        result = []
        l1, c1, l2, c2  = ("a", a, "b", b) if a > b else ("b", b, "a", a)
        while c1 > 0 and c2 > 0:
            if c1 < c1:
                result.append(l1 + 2 * l2)
                c1 -= 1
                c2 -= 2
            elif c2 < c1:
                result.append(2 * l1 + l2)
                c1 -= 2
                c2 -= 1
            else:
                result.append(l1 + l2)
                c1 -= 1
                c2 -= 1
        
        if c1 > 0:
            result.append(c1 * l1)
        if c2 > 0:
            result.append(c2 * l2)
        
        return "".join(result)

