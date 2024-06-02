class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for n in nums:
            if n != 0:
                nums[pos] = n
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0
        
        
