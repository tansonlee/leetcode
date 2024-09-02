class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        total_sum = sum(chalk)

        num_full_cycles = k // total_sum
        k -= total_sum * num_full_cycles


        while True:
            if k < chalk[i]:
                return i
            
            k -= chalk[i]

            i = (i + 1) % len(chalk)

        
