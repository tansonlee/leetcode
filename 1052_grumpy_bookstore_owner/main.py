class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        curr = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                curr += customers[i]
            elif grumpy[i] == 1 and i < minutes:
                curr += customers[i]
        result = curr

        for i in range(len(customers) - minutes):
            front = customers[i + minutes] if grumpy[i + minutes] == 1 else 0
            back = customers[i] if grumpy[i] == 1 else 0
            curr += front - back
            result = max(result, curr)

        return result

        
