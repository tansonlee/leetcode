class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        
        opens = 0

        for c in s:
            if c == "(":
                opens += 1
                stack.append(c)
            elif c == ")":
                if opens > 0:
                    stack.append(c)
                    opens -= 1
            else:
                stack.append(c)

        other_stack = []
        while opens > 0:
            c = stack.pop()
            if c == "(":
                opens -= 1
            else:
                other_stack.append(c)
        
        while other_stack:
            stack.append(other_stack.pop())
        
        return "".join(stack)

