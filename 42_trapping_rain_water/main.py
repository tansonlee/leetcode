class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]

        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        
        for i in reversed(range(1, len(height) - 1)):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        result = 0
        for i in range(len(height)):
            result += max(0, min(left_max[i], right_max[i]) - height[i])
        return result


        
