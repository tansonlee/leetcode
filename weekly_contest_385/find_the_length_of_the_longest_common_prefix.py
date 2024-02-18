class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def lcp(n1, n2):
            for i in range(min(len(n1), len(n2))):
                if n1[i] != n2[i]:
                    return i
            return min(len(n1), len(n2))
        
        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]
        arr1.sort()
        arr2.sort()
        
        p1, p2 = 0, 0
        result = 0
        while p1 < len(arr1) and p2 < len(arr2):
            result = max(result, lcp(arr1[p1], arr2[p2]))
            
            if arr1[p1] < arr2[p2]:
                p1 += 1
            else:
                p2 += 1
                
        return result
                
        
