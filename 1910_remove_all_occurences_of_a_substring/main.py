class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        ##### 
        # Stack solution
        #####
        stack = []

        def stack_top_eq(stack, string):
            if len(stack) < len(string):
                return False
            for i in range(1, len(string) + 1):
                if stack[-i] != string[-i]:
                    return False
            return True


        for char in s:
            stack.append(char)

            # check the last len(part) characters of the stack
            while stack_top_eq(stack, part):
                for _ in range(len(part)):
                    stack.pop()
        
        return "".join(stack)

        #####
        # String slicing solution
        #####
        index = 0
        while index < len(s):
            if s[index:index + len(part)] == part:
                s = s[:index] + s[index + len(part):]
                index -= max(0, len(part))
            else:
                index += 1
        
        return s

