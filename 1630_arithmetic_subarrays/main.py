class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic_subarray(arr, start, end):
            minimum = float("inf")
            maximum = float("-inf")
            for i in range(start, end):
                minimum = min(minimum, arr[i])
                maximum = max(maximum, arr[i])
            if minimum == maximum:
                return True
            n = end - start
            if n == 1:
                return True
            if (maximum - minimum) % (n - 1) != 0:
                return False
            d = (maximum - minimum) // (n - 1)

            s = set()
            for i in range(start, end):
                if arr[i] in s:
                    return False
                if (arr[i] - minimum) % d != 0:
                    return False
                s.add(arr[i])
            return True
        
        result = [False for _ in range(len(l))]

        for i in range(len(l)):
            result[i] = is_arithmetic_subarray(nums, l[i], r[i] + 1)
        
        return result


        
