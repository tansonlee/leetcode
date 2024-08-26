class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # Whether you can split the input given the number of digits for the denominator
        def max_message_length(digits):
            # From 1-9, we can support limit - digits - 5 each (9)
            # From 10-99, we can support limit - digits - 6 each (90)
            # From 100-999, we can support limit - digits - 7 each (900)

            result = 0
            for i in range(1, digits + 1):
                result += (limit - digits - 3 - i) * (9 * (10 ** (i - 1)))
            
            return result 
        
        # Determine the denominator
        def get_denominator(denominator_digits):
            # Determine the characters taken from parts that have a numerator with fewer digits than denominator
            taken = 0
            for i in range(1, denominator_digits):
                taken += (limit - denominator_digits - 3 - i) * (9 * (10 ** (i - 1)))
            
            remaining = len(message) - taken
            # How many parts will have the numerator the same length as the denominator
            use = ceil(remaining / (limit - denominator_digits - 3 - denominator_digits))

            return 10 ** (denominator_digits - 1) + use - 1
        
        def split_message(denominator):
            result = []
            part = 1
            ptr = 0
            while ptr < len(message):
                length = limit - len(str(part)) - len(str(denominator)) - 3
                result.append(f"{message[ptr: ptr + length]}<{part}/{denominator}>")
                part += 1
                ptr += length
            
            return result
    
        denominator_digits = 1

        while len(message) > max_message_length(denominator_digits):
            denominator_digits += 1
            if denominator_digits > limit:
                return [] # Impossible
        
        denominator = get_denominator(denominator_digits)

        return split_message(denominator)
        
