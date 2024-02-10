class RandomizedSet:
    def __init__(self):
        self.d = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.arr)
        self.arr.append(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.d:
            return False
        last_val = self.arr[-1]
        curr_val_idx = self.d[val]
        self.arr[curr_val_idx] = last_val
        self.d[last_val] = curr_val_idx
        del self.d[val]
        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
