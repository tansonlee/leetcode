class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = dict([(n, i + 1) for i, n in enumerate(sorted(list(set(arr))))])

        return [ranks[n] for n in arr]
        
