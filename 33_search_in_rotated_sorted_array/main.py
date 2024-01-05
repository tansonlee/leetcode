class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def find_min_index(nums):
            left = 0
            right = len(nums) - 1
    
            while left < right:
                if nums[left] < nums[right]:
                    return left

                mid_index = (left + right) // 2
                if left == mid_index:
                    break
                if nums[left] < nums[mid_index]:
                    left = mid_index
                if nums[left] > nums[mid_index]:
                    right = mid_index
            
            return (left + 1) % len(nums)
        
        min_index = find_min_index(nums)
        left = min_index
        right = left + len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid % len(nums)] == target:
                return mid % len(nums)
            elif nums[mid % len(nums)] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


        
