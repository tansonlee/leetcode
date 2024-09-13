class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cumulative = [arr[0]]
        
        for i in range(1, len(arr)):
            cumulative.append(cumulative[-1] ^ arr[i])
        
        result = []
        for left, right in queries:
            curr = cumulative[right]
            if left > 0:
                curr ^= cumulative[left - 1]
            result.append(curr)
        return result

        
