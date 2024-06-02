class SparseVector:
    def __init__(self, nums: List[int]):
        self.values = {}
        for i in range(len(nums)):
            if nums[i]:
                self.values[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i in self.values:
            if i in vec.values:
                result += self.values[i] * vec.values[i]
        return result


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
