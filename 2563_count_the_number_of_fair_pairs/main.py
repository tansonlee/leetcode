class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        result = 0
        for i in range(len(nums)):
            # Find the index a such that nums[a] is minimized
            # and lower <= nums[i] + nums[a]
            a = bisect_left(nums, lower - nums[i], lo=0, hi=i)

            # Find the index b such that nums[b] is maximized 
            # and nums[i] + nums[b] <= upper
            b = bisect_right(nums, upper - nums[i], lo=0, hi=i)

            result += b - a
        
        return result

        
