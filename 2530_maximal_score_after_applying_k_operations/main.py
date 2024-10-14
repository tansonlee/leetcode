class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-1 * x for x in nums] # make max heap
        heapify(nums)

        result = 0
        for _ in range(k):
            top = heappop(nums) * -1
            result += top
            heappush(nums, -ceil(top / 3))

        return result


        
