class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def hash(string):
            result = []
            for i in range(len(string) - 1):
                result.append((ord(string[i + 1]) - ord(string[i])) % 26)
            return tuple(result)
        
        hash_to_values = defaultdict(list)
        for s in strings:
            hash_to_values[hash(s)].append(s)
        
        result = []
        for h in hash_to_values:
            result.append(hash_to_values[h])
        
        return result

        
