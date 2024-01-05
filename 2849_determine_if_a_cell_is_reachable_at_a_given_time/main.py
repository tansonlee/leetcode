class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy and t == 1:
            return False

        dx = abs(sx - fx)
        dy = abs(sy - fy)

        return t >= max(dx, dy)


