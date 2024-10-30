class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Find number of elements in a ramp ending at i
        # from left to right and right to left
        n = len(nums)

        left_to_right = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left_to_right[i] = max(left_to_right[i], left_to_right[j] + 1)

        right_to_left = [1 for _ in range(n)]
        for i in reversed(range(n)):
            for j in reversed(range(i + 1, n)):
                if nums[j] < nums[i]:
                    right_to_left[i] = max(right_to_left[i], right_to_left[j] + 1)
        
        # Now at a given number, look at the left and right ramps and find the best
        result = inf

        for i in range(n):
            left = left_to_right[i]
            right = right_to_left[i]

            if left > 1 and right > 1:
                # Minus 1 because reusing the current num.
                total_used = left + right - 1
                to_remove = n - total_used
    
                result = min(result, to_remove)
        
        return result


