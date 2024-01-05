class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        result = {}
        
        for n in sorted_arr:
            result[n] = 1

        for i in range(len(sorted_arr)):
            n = sorted_arr[i]
            for j in range(0, i + 1):
                a = sorted_arr[j]
                if n % a != 0:
                    continue
                b = n / a
                if b not in result:
                    continue
                result[n] += (result[a] * result[b])
        
        count = 0
        for n in result:
            count += result[n]
        
        return count % (10 ** 9 + 7)






        
