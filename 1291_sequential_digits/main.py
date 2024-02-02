# so ugly 
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def seq_nums_with_digits(digits):
            if digits > 9:
                return []
            result = []
            curr = 0
            maximum = digits
            for i in range(digits):
                curr *= 10
                curr += i + 1
            result.append(curr)

            while maximum < 9:
                maximum += 1
                curr = curr % (10 ** (digits - 1))
                curr *= 10
                curr += maximum
                result.append(curr)
            return result
        
        result = []
        len_low = len(str(low))
        len_high = len(str(high))

        for i in range(len_low, len_high + 1):
            ds = seq_nums_with_digits(i)
            for n in ds:
                if n >= low and n <= high:
                    result.append(n)
        
        return result
