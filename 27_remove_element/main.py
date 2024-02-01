class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        back = len(nums) - 1
        curr = 0

        while curr < back:
            if nums[curr] == val:
                while back > curr and nums[back] == val:
                    back -= 1
                nums[back], nums[curr] = nums[curr], nums[back]
            else:
                curr += 1
        
        if curr < len(nums) and nums[curr] == val:
            return curr
        return curr + 1
        
