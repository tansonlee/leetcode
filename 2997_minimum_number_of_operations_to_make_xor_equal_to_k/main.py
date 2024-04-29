class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def bit(n, pos):
            return (n >> pos) & 1
        
        result = 0
        for i in range(20): # 20 is max number of bits to represent nums[i]
            num_ones = 0
            for n in nums:
                if bit(n, i):
                    num_ones += 1
            if bit(k, i) and num_ones % 2 == 0 or not bit(k, i) and num_ones % 2 == 1:
                result += 1
        
        return result

        
