from typing import List

class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        subs = []
        curr = []
        for i in range(len(nums) - 1):
            curr.append(nums[i])
            if nums[i] == nums[i+1]:
                subs.append(curr)
                curr = []
        curr.append(nums[len(nums) - 1])
        if curr:
            subs.append(curr)
        
        result = 0
        for s in subs:
            result += (len(s) * (len(s) + 1)) // 2
        return result
        

s = Solution()
print(s.countAlternatingSubarrays([0,1,1,1]))
print(s.countAlternatingSubarrays([1,0,1,0]))
