class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def pos_to_placement(pos):
            if pos == 0:
                return "Gold Medal"
            if pos == 1:
                return "Silver Medal"
            if pos == 2:
                return "Bronze Medal"
            return str(pos + 1)
        
        class Chainer:
            def __init__(self, arr):
                self.arr = arr
            
            def sort(self, key, reverse):
                self.arr.sort(key=key, reverse=reverse)
                return self
            
            def map(self, fn):
                self.arr = list(map(fn, self.arr))
                return self
            
            def enumerate(self):
                self.arr = list(enumerate(self.arr))
                return self
            
            def get(self):
                return self.arr
        
        return Chainer(score) \
            .enumerate() \
            .sort(lambda x: x[1], True) \
            .enumerate() \
            .map(lambda x: (x[1][0], pos_to_placement(x[0]))) \
            .sort(lambda x: x[0], False) \
            .map(lambda x: x[1]) \
            .get()

