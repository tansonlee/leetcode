class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or self.map[key][0][1] > timestamp:
            return ""
        
        # Perform a binary search such that timestamp is just larger.
        values = self.map[key]

        def get_time_at(index):
            if index < 0:
                return -inf
            if index >= len(values):
                return inf
            
            return values[index][1]

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if get_time_at(mid) <= timestamp < get_time_at(mid + 1):
                return values[mid][0]
          
            if get_time_at(mid) < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
