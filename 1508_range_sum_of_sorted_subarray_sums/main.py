class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for start in range(len(nums)):
            curr_sum = nums[start]
            subarray_sums.append(curr_sum)
            for end in range(start + 1, len(nums)):
                curr_sum += nums[end]
                subarray_sums.append(curr_sum)
        
        subarray_sums.sort()
        return sum(subarray_sums[left - 1:right]) % (10 ** 9 + 7)

        
