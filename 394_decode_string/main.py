class Solution:
    def decodeString(self, s: str) -> str:
        def helper(s):
            result = []
    
            index = 0
            while index < len(s):
                if s[index].isalpha():
                    result.append(s[index])
                    index += 1
                else: # hit a number
                    # Extract the number
                    number_end = index
                    while s[number_end].isnumeric():
                        number_end += 1
                    number = int(s[index: number_end])
    
                    # Extract the part to repeat
                    repeat_start = number_end + 1
                    repeat_end = repeat_start
                    depth = 1
                    while depth != 0:
                        if s[repeat_end] == '[':
                            depth += 1
                        elif s[repeat_end] == ']':
                            depth -= 1
                        repeat_end += 1
                    index = repeat_end
                    repeat_end -= 1
                    repeat = helper(s[repeat_start: repeat_end])
    
                    result.extend(repeat * number)

            return result
        
        return "".join(helper(s))




        
