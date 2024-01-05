class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        mid_week_start = full_weeks / 2
        overflow_num_days = n % 7

        a = ((mid_week_start + (mid_week_start + 7)) * (7/2)) * full_weeks
        b = ((full_weeks + 1) + (full_weeks + overflow_num_days)) * (overflow_num_days / 2)
        
        return int(a + b)
        
