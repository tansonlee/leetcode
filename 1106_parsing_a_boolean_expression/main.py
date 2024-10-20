class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            if expression == 't':
                return True 
            elif expression == 'f':
                return False
            else:
                raise Exception("Invalid boolean literal")
        
        # x(<subexpr>)
        # where x is an operation
        sub_exprs = self.parse_sub_expr(expression[2:-1])

        op = expression[0]
        
        if op == '!':
            return not self.parseBoolExpr(sub_exprs[0])
        elif op == '&':
            result = True 
            for expr in sub_exprs:
                result = result and self.parseBoolExpr(expr)
            return result
        elif op == '|':
            result = False
            for expr in sub_exprs:
                result = result or self.parseBoolExpr(expr)
            return result

        raise Exception("Invalid op", op)
    
    def parse_sub_expr(self, expression):
        result = []
        ptr = 0
        while ptr < len(expression):
            sub_expr_end = self.parse_single_expr(expression, ptr)
            result.append(expression[ptr:sub_expr_end])
            ptr = sub_expr_end
            ptr += 1 # To skip the comma
        
        return result
    
    def parse_single_expr(self, expression, ptr):
        if expression[ptr] == 't' or expression[ptr] == 'f':
            return ptr + 1
        
        # x(...)
        open_parens = 1
        for i in range(ptr + 2, len(expression)):
            if expression[i] == '(':
                open_parens += 1
            elif expression[i] == ')':
                open_parens -= 1

            if open_parens == 0:
                return i + 1
        
        raise Exception("Could not parse single expression", expression, ptr)
        

