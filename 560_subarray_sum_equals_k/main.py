from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        
        counts = defaultdict(int)
        counts[0] = 1
        result = 0
        for num in nums:
            if (num - k) in counts:
                result += counts[num - k]
            counts[num] += 1
        return result

        
        
