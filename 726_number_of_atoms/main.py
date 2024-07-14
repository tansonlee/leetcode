class Solution:
    def countOfAtoms(self, formula: str) -> str:
        index = 0

        def parse_count():
            nonlocal index

            count = ""
            while index < len(formula) and formula[index].isdigit():
                count += formula[index]
                index += 1
            count = int(count) if len(count) else 1
            return count

        def count_atoms():
            nonlocal index

            result = defaultdict(int)

            while index < len(formula):
                if formula[index] == ')':
                    return result # Finished parsing nested formula

                if formula[index] == '(': # Case 1: nested element formula
                    index += 1 # consume '('
                    inner_counts = count_atoms()
                    index += 1 # consume ')'

                    count = parse_count()
                    
                    for k in inner_counts:
                        result[k] += inner_counts[k] * count
                else:                     # Case 2: top level element formula
                    # Get element name.
                    name = formula[index]
                    index += 1
                    while index < len(formula) and formula[index].islower():
                        name += formula[index]
                        index += 1
                    
                    count = parse_count()
                    result[name] += count
            
            return result
                
        total_count = count_atoms()
        listed = [(name, total_count[name]) for name in total_count]
        listed.sort()

        return "".join([f"{name}{count if count > 1 else ''}" for name, count in listed])
        
