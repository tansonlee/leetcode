class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(n_open, n_close, curr):
            if n_open == 0 and n_close == 0:
                result.append(curr)
            if n_close == 0:
                return
            
            if n_open > 0:
                helper(n_open - 1, n_close, curr + "(")
            
            if n_close > 0 and n_close > n_open:
                helper(n_open, n_close - 1, curr + ")")

        helper(n, n, "")
        return result

