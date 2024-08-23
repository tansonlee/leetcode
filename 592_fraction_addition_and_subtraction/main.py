class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Starting from i, parse a fraction.
        def get_num(s, i):
            sign = -1 if s[i] == '-' else 1
            if sign == -1:
                i += 1
            
            numerator = ""
            while s[i].isdigit():
                numerator += s[i]
                i += 1
            
            i += 1 # consume the '/'

            denominator = ""
            while i < len(s) and s[i].isdigit():
                denominator += s[i]
                i += 1
            
            return (sign * int(numerator), int(denominator)), i
        
        # Simplify a fraction to its lowest form.
        def simplify(fraction):
            num = fraction[0]
            den = fraction[1]

            if num == 0:
                return (0, 1)
            
            sign = 1 if num > 0 else -1
            if sign == -1:
                num *= -1

            divisor = 2

            while divisor <= min(num, den):
                if num % divisor == 0 and den % divisor == 0:
                    num //= divisor
                    den //= divisor
                else:
                    divisor += 1
            
            return (num * sign, den)

        def evaluate(fractions):
            curr = (0, 1)
            for num, den in fractions:
                curr = (num * curr[1] + curr[0] * den, den * curr[1])
                print(curr)
                curr = simplify(curr)
            
            return curr

        fractions = []
        i = 0
        frac, i = get_num(expression, i)
        fractions.append(frac)
        while i < len(expression):
            sign = 1 if expression[i] == '+' else -1
            i += 1
            frac, i = get_num(expression, i)
            fractions.append((sign * frac[0], frac[1]))
            if i == len(expression):
                break

        result = evaluate(fractions)

        return f"{result[0]}/{result[1]}"
        
