class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = collections.defaultdict(int)
        for n in arr:
            counts[n] += 1
        
        counts_and_num = []
        for n in counts:
            counts_and_num.append((counts[n], n))
        
        counts_and_num.sort(reverse=True)

        for i in reversed(range(len(counts_and_num))):
            k -= counts_and_num[i][0] 
            if k < 0:
                return i + 1
        
        return 0
