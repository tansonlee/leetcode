class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Answer is the longest run of the max element.
        m = max(nums)

        result = 0
        curr = 0
        for n in nums:
            if n == m:
                curr += 1
                result = max(result, curr)
            else:
                curr = 0

        return result

        
