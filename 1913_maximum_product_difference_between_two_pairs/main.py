class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = nums.index(max(nums))
        max2 = -1
        for i in range(len(nums)):
            if i != max1:
                if max2 == -1 or nums[i] > nums[max2]:
                    max2 = i
        
        min1 = nums.index(min(nums))
        min2 = -1
        for i in range(len(nums)):
            if i != min1:
                if min2 == -1 or nums[i] < nums[min2]:
                    min2 = i

        return (nums[max1] * nums[max2]) - (nums[min1] * nums[min2])
        

