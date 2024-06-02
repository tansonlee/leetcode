class Solution:
    def romanToInt(self, s: str) -> int:
        s_to_v = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0

        for i in range(len(s) - 1):
            curr_val = s_to_v[s[i]]
            next_val = s_to_v[s[i + 1]]

            if curr_val >= next_val:
                result += curr_val
            else:
                result -= curr_val
        result += s_to_v[s[-1]]
        return result




        
