from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        result = nums[0]
        for n in counts:
            if counts[n] > counts[result]:
                result = n
        
        return result

