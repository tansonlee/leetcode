class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        spaces = set(spaces)
        for i in range(len(s)):
            if i in spaces:
                result.append(" ")
            result.append(s[i])
        return "".join(result)
        
