class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can_do(k):
            prev_ball = position[0]
            left = m - 1
            for p in position:
                if p - prev_ball >= k:
                    left -= 1
                    prev_ball = p
                if left == 0:
                    return True
            return False
        
        lower = 1
        upper = max(position)
        ans = -1

        while lower <= upper:
            mid = (lower + upper) // 2
            if can_do(mid):
                ans = mid
                lower = mid + 1
            else:
                upper = mid - 1

        return ans 
                
                
        
