class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find left
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        begin = None
        if right + 1 < len(nums) and nums[right + 1] == target:
            begin = right + 1
        if begin is None:
            begin = -1

        # find right
        left = 0 
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        
        end = None
        if left - 1 >= 0 and nums[left - 1] == target:
            end = left - 1
        if end is None:
            end = -1

        return [begin, end]


        
