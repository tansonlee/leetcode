from collections import defaultdict

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnts = defaultdict(int)

        for n in nums:
            cnts[n] += 1

        result = []

        for n in cnts:
            for i in range(cnts[n]):
                if len(result) <= i:
                    result.append([])
                result[i].append(n)
        
        return result

        
