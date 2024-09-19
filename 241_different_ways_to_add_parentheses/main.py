class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        tokens = []
        curr = 0
        for i in range(len(expression)):
            char = expression[i]
            if char.isdigit():
                curr = curr * 10 + int(char)
            else:
                tokens.append(curr)
                curr = 0
                tokens.append(char)
        
        tokens.append(curr)
            
        def do_op(a, b, op):
            if op == '+':
                return a + b
            if op == '-':
                return a - b
            if op == '*':
                return a * b
        
        def get_results(nums):
            if len(nums) == 1:
                return [nums[0]]
            
            if len(nums) == 3:
                return [do_op(nums[0], nums[2], nums[1])]
            
            result = []
            # For each operator index
            for i in range(1, len(nums), 2):
                left = get_results(nums[:i])
                right = get_results(nums[i + 1:])
                op = nums[i]

                for l in left:
                    for r in right:
                        result.append(do_op(l, r, op))

            return result
        
        return get_results(tokens)
        
