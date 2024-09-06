from sortedcontainers import SortedList

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        seen = SortedList([nums[0]])

        def find_closest(sorted_list, n):
            pos = bisect.bisect_left(sorted_list, n)
        
            if pos == 0:
                return sorted_list[0]
            if pos == len(sorted_list):
                return sorted_list[-1]
        
            before = sorted_list[pos - 1]
            after = sorted_list[pos]
        
            if after - n < n - before:
                return after
            else:
                return before

        result = inf
        for i in range(x, len(nums)):
            num = nums[i]
            result = min(result, abs(num - find_closest(seen, num)))
            seen.add(nums[i - x + 1])
        
        return result


        
