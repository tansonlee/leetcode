class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Meeting rooms 2
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, 0))
        
        events.sort()
        
        result = 0
        curr = 0
        for _, kind in events:
            if kind == 0:
                curr -= 1
            else:
                curr += 1
            result = max(result, curr)
        
        return result


        
