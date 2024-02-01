class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        spacing = 2 + (numRows - 2) * 2
        result = ""

        def get_if_exists(s, idx):
            if idx >= 0 and idx < len(s):
                return s[idx]
            return ""

        for offset in range(numRows):
            for i in range(0, len(s) + spacing, spacing):
                if offset == 0:
                    result += get_if_exists(s, i)
                elif offset == numRows - 1:
                    result += get_if_exists(s, i + offset)
                else:
                    result += get_if_exists(s, i - offset)
                    result += get_if_exists(s, i + offset)
        
        return result

