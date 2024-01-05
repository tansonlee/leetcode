class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] - int(str(nums[i])[::-1])
        
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        
        result = 0
        for key in freq:
            val = freq[key]
            result += (val * (val - 1)) // 2

        return result % (10 ** 9 + 7)

