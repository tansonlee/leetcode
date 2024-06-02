class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")

        stack = []
        for p in parts:
            if len(p) == 0:
                continue
            elif p == ".":
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        
        return "/" + "/".join(stack)
            
        
