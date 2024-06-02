class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        tokens = []
        curr_type = 'number' if abbr[0].isnumeric() else 'string'
        curr_number = 0
        curr_string = ''

        i = 0
        while i < len(abbr):
            if curr_type == 'number':
                if abbr[i].isnumeric():
                    if curr_number == 0 and int(abbr[i]) == 0:
                        return False
                    curr_number = curr_number * 10 + int(abbr[i])
                    i += 1
                else:
                    tokens.append(('number', curr_number))
                    curr_number = 0
                    curr_type = 'string'
            else:
                if not abbr[i].isnumeric():
                    curr_string += abbr[i]
                    i += 1
                else:
                    tokens.append(('string', curr_string))
                    curr_string = ''
                    curr_type = 'number'
        
        if curr_number:
            tokens.append(('number', curr_number))
        elif curr_string:
            tokens.append(('string', curr_string))
            
        i = 0
        for typ, val in tokens:
            if typ == 'string':
                for c in val:
                    if i >= len(word) or word[i] != c:
                        print("string", i, c)
                        return False
                    i += 1
            if typ == 'number':
                if val + i > len(word):
                    print("number", i, val)
                    return False
                i += val

        return i == len(word)


