class Solution:
    def knightDialer(self, n: int) -> int:
        nums = [1 for _ in range(10)]

        for i in range(n - 1):
            next_nums = [0 for _ in range(10)]
            next_nums[0] = nums[4] + nums[6]
            next_nums[1] = nums[8] + nums[6]
            next_nums[2] = nums[7] + nums[9]
            next_nums[3] = nums[4] + nums[8]
            next_nums[4] = nums[3] + nums[9] + nums[0]
            next_nums[5] = 0
            next_nums[6] = nums[1] + nums[7] + nums[0]
            next_nums[7] = nums[2] + nums[6]
            next_nums[8] = nums[1] + nums[3]
            next_nums[9] = nums[4] + nums[2]

            nums = next_nums
        
        return sum(nums) % (10 ** 9 + 7)


        
