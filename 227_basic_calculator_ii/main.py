class Solution:
    def calculate(self, s: str) -> int:
        # first split s into an array of tokens
        tokens = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            
            if s[i] in "+-*/":
                tokens.append(s[i])
                i += 1
                continue
            
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            tokens.append(num)

        stack = [int(tokens[0])]

        for t in tokens[1:]:
            if t in "+-*/":
                stack.append(t) # indicate last seen operation
                continue

            op = stack.pop()
            if op == '+':
                stack.append(int(t))
            elif op == "-":
                stack.append(-int(t))
            elif op == "*":
                stack.append(stack.pop() * int(t))
            elif op == "/":
                stack.append(int(stack.pop() / int(t)))

        return sum(stack)


