class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def do(a, b):
            m = {}
            for i in range(len(a)):
                if a[i] not in m:
                    m[a[i]] = b[i]
                else:
                    if m[a[i]] != b[i]:
                        return False
            return True
        
        return do(s, t) and do(t, s)

