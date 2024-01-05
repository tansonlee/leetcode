class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        curr = 0
        arr.sort()
        for i in range(len(arr)):
            arr[i] = min(curr + 1, arr[i])
            curr = arr[i]
        return arr[-1]
        
