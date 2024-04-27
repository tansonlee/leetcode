class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        @cache
        def helper(key, curr):
            if len(key) == 0:
                return 0

            c = key[0]
            left_steps = 0
            while ring[(curr - left_steps) % len(ring)] != c:
                left_steps += 1

            right_steps = 0
            while ring[(curr + right_steps) % len(ring)] != c:
                right_steps += 1
            
            left_curr = (curr - left_steps) % len(ring)
            right_curr = (curr + right_steps) % len(ring)
            return min(left_steps + helper(key[1:], left_curr), right_steps + helper(key[1:], right_curr))
                
        return helper(key, 0) + len(key)
        
