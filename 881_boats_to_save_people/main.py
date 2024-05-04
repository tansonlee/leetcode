class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        result = 0

        while left < right:
            if people[left] + people[right] <= limit:
                result += 1
                left += 1
                right -= 1
            else:
                result += 1
                right -= 1
        if left == right:
            result += 1
        
        return result
            

        
