class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Find a and b such that
        # arr[:a+1] is non-decreasing
        # arr[b:] is non-decreasing
        a = 1
        while a < len(arr) and arr[a - 1] <= arr[a]:
            a += 1
        a -= 1
        
        b = len(arr) - 1
        while b > 0 and  arr[b - 1] <= arr[b]:
            b -= 1
        
        if b <= a:
            return 0
        
        result = min(len(arr) - a - 1, b)
        left = 0
        right = b
        while left <= a and right < len(arr):
            if arr[left] <= arr[right]:
                result = min(result, right - left - 1)
                left += 1
            else:
                right += 1
        
        return result

        


        
