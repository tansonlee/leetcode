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


class Solution:
    def calculate(self, s: str) -> int:
        parsed = []
        curr_num = 0
        for c in s:
            if c == " ":
                continue
            if c in "+-*/":
                parsed.append(curr_num)
                curr_num = 0
                parsed.append(c)
            else:
                curr_num = 10 * curr_num + int(c)
        parsed.append(curr_num)

        # pass 1 for mult and div
        stack1 = list(reversed(parsed))
        stack2 = []

        while stack1:
            top = stack1.pop()
            if str(top) in "*/":
                left = stack2.pop()
                right = stack1.pop()
                if top == "*":
                    stack2.append(left * right)
                else:
                    stack2.append(left // right)
            else:
                stack2.append(top)
        
        # pass 2 for add and sub
        result = stack2[0]
        for i in range(1, len(stack2), 2):
            if stack2[i] == "+":
                result += stack2[i+1]
            else:
                result -= stack2[i+1]
            
        return result
