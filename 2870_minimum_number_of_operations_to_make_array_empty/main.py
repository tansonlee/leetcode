from collections import defaultdict

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnts = defaultdict(int)
        for n in nums:
            cnts[n] += 1
        result = 0
        for n in cnts:
            ct = cnts[n]
            if ct == 1:
                return -1
            if ct % 3 == 0:
                result += ct // 3
            elif ct % 3 == 1:
                result += (ct // 3) - 1 + 2
            elif ct % 3 == 2:
                result += (ct // 3) + 1

        return result
            
            
            
        
