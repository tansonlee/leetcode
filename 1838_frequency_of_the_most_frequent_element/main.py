class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        nums.sort()
        left = len(nums) - 1
        right = left
        result = -1

        while left > 0:
            target = nums[right]
            while True:
                if left == 0 or target - nums[left - 1] > k:
                    break
                k -= (target - nums[left - 1])
                left -= 1

            result = max(result, right - left + 1)
            right -= 1
            k += (right - left + 1) * (nums[right + 1] - nums[right])

        return result

