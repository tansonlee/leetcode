class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        def get_tup(s):
            result = [0 for _ in range(26)]
            for char in s:
                result[ord(char) - ord('a')] += 1
            return tuple(result)
        
        for s in strs:
            t = get_tup(s)
            if t not in groups:
                groups[t] = []
            groups[t].append(s)
        
        result = []
        for key in groups:
            result.append(groups[key])
        
        return result

