class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def set_bit(x, c):
            return x | (1 << ord(c) - ord('a'))

        def get_mask(s):
            result = 0
            for c in s:
                result = set_bit(result, c)
            return result

        no_dupes = []
        for s in arr:
            if len(s) == len(set(s)):
                no_dupes.append(s)
        arr = no_dupes

        arr = [get_mask(x) for x in arr]

        results = [0]
        for s in arr:
            l = len(results)
            for i in range(l):
                if s & results[i] == 0:
                    results.append(results[i] | s)
        
        result = 0
        for s in results:
            if s.bit_count() > result.bit_count():
                result = s
        return result.bit_count()

