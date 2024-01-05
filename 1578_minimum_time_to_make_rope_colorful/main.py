
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        curr = 0
        while curr < len(colors):
            curr_color = colors[curr]
            candidates = []
            while curr < len(colors) and colors[curr] == curr_color:
                candidates.append(neededTime[curr])
                curr += 1
            
            result += sum(candidates)
            result -= max(candidates)
        
        return result

