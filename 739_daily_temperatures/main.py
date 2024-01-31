class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        s = []

        for i in reversed(range(len(temperatures))):
            while len(s) and s[-1][0] <= temperatures[i]:
                s.pop()
            
            if len(s):
                result[i] = s[-1][1] - i

            s.append((temperatures[i], i))
        
        return result

