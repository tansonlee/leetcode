class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(idx):
            if idx == -1 or idx == len(nums):
                return float("-inf")
            return nums[idx]
        front = 0
        back = len(nums) - 1

        while front <= back:
            mid = (front + back) // 2
            if get(mid - 1) < get(mid) and get(mid) > get(mid + 1):
                return mid
            
            if get(mid) < get(mid + 1):
                front = mid + 1
            else:
                back = mid - 1
            
        
        
