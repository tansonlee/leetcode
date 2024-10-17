class Solution:
    def maximumSwap(self, num: int) -> int:
        def num_to_list(num):
            digits = []
            while num > 0:
                digits.append(num % 10)
                num //= 10
            
            digits.reverse()
            return digits
        
        def list_to_num(lst):
            result = 0
            for n in lst:
                result = result * 10 + n
            return result
        
        digits = num_to_list(num)
        max_digits = sorted(digits, reverse=True)

        swap_index = -1
        swap_val = -1
        for i in range(len(digits)):
            if digits[i] != max_digits[i]:
                swap_index = i
                swap_val = max_digits[i]
                break
        
        if swap_index == -1:
            return num
        
        # Find index of last occurance of swap_val
        index = len(digits) - 1 - digits[::-1].index(swap_val)
        
        digits[swap_index], digits[index] = digits[index], digits[swap_index]

        return list_to_num(digits)

        

