class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        ptr = 0

        while ptr < len(words):
            # Determine what words belong on this line
            line = []
            line_length = 0 # not including any spaces
            while ptr < len(words):
                # There are len(line) - 1 minimum spaces
                curr_line_length = line_length + len(line) - 1

                if curr_line_length + len(words[ptr]) + 1 > maxWidth:
                    break
                
                line.append(words[ptr])
                line_length += len(words[ptr])
                ptr += 1

            # Special case for one word on a line
            if len(line) == 1:
                result.append(line[0] + " " * (maxWidth - len(line[0])))
                continue
            
            # Special case for last line
            if ptr >= len(words):
                last_line = " ".join(line)
                result.append(last_line + " " * (maxWidth - len(last_line)))
                continue
            
            # Create an array of spaces
            total_spaces = maxWidth - line_length

            min_space = total_spaces // (len(line) - 1)
            additional_spaces = total_spaces - (min_space * (len(line) - 1))

            spaces = [" " * (min_space + 1)] * additional_spaces + [" " * min_space] * (len(line) - 1 - additional_spaces)
            spaces.append("") # So that zip is happy

            line_result = []
            for word, space in zip(line, spaces):
                line_result.append(word)
                line_result.append(space)
            result.append("".join(line_result))
        
        return result
                

        
