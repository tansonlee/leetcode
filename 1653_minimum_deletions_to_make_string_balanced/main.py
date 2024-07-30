class Solution:
    def minimumDeletions(self, s: str) -> int:
        cumulative_a = [0 for _ in range(len(s))]
        cumulative_b = [0 for _ in range(len(s))]

        if s[0] == 'a':
            cumulative_a[0] = 1
        else:
            cumulative_b[0] = 1

        for i in range(1, len(s)):
            if s[i] == 'a':
                cumulative_a[i] = cumulative_a[i - 1] + 1
                cumulative_b[i] = cumulative_b[i - 1]
            else:
                cumulative_a[i] = cumulative_a[i - 1]
                cumulative_b[i] = cumulative_b[i - 1] + 1
        
        def bs_before(i):
            if i == 0:
                return 0
            return cumulative_b[i - 1]
    
        def as_after(i):
            return cumulative_a[-1] - cumulative_a[i]
        
        result = inf
        for i in range(len(s)):
            result = min(result, bs_before(i) + as_after(i))
        
        return result


        
