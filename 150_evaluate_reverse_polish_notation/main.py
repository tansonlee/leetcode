class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for t in tokens:
            if t == "+" or t == "-" or t == "*" or t == "/":
                n1 = s.pop()
                n2 = s.pop()
                if t == "+":
                    s.append(n2 + n1)
                elif t == "-":
                    s.append(n2 - n1)
                elif t == "*":
                    s.append(n2 * n1)
                elif t == "/":
                    r = n2 / n1
                    if r < 0:
                        s.append(ceil(r))
                    else:
                        s.append(floor(r))
            else:
                s.append(int(t))
        return s[0]
        
