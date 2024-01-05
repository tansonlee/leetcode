class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        
        is_increasing = None
        curr = nums[0]

        for n in nums:
            if n > curr:
                if is_increasing == False:
                    return False
                is_increasing = True
                curr = n
            elif n < curr:
                if is_increasing == True:
                    return False
                is_increasing = False
                curr = n

        return True

        
