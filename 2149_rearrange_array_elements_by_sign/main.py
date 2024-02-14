class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for n in nums:
            if n < 0:
                negatives.append(n)
            else:
                positives.append(n)
        
        result = []
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(positives[i // 2])
            else:
                result.append(negatives[i // 2])
        return result

        
