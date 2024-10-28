class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        links = {}

        for n in nums:
            links[n] = None
        
        for n in nums:
            sqrt = int(math.sqrt(n))
            if sqrt * sqrt != n:
                continue
            if sqrt in links:
                links[sqrt] = n
        
        visited = set()

        def longest_chain(n):
            if n not in links:
                return 0
            visited.add(n)

            return 1 + longest_chain(links[n])
        
        result = 0
        for n in links:
            if n in visited:
                continue
            result = max(result, longest_chain(n))
            
        if result == 1:
            return -1
        return result





        
