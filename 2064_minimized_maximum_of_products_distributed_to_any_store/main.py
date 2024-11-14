class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        # Can we distribute it such that each store has at most x products
        def works(x):
            store_count = 0

            for q in quantities:
                store_count += ceil(q / x)

                if store_count > n:
                    return False
            
            return True
        
        # Binary search for x
        left = 1
        right = max(quantities)

        while left < right:
            mid = (left + right) // 2

            if works(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

        
