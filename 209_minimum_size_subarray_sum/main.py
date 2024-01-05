class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        front = 0
        back = 0
        curr_sum = nums[0]
        result = 1 if curr_sum >= target else float("inf")

        while back < len(nums) and front < len(nums):
            if (curr_sum < target or front == back) and back < len(nums) - 1:
                back += 1
                curr_sum += nums[back]
            else:
                curr_sum -= nums[front]
                front += 1
            
            if curr_sum >= target:
                result = min(result, back - front + 1)
        
        return result if result != float("inf") else 0


        
