class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cumulative = 0
        seen = defaultdict(int)
        seen[0] = 1
        result = 0

        for n in nums:
            cumulative += n
            result += seen[cumulative % k]
            seen[cumulative % k] += 1
        
        return result


