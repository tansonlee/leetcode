class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        result = []

        for n in c1:
            for _ in range(min(c1[n], c2[n])):
                result.append(n)
        return result
        
