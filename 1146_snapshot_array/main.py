class SnapshotArray:

    def __init__(self, length: int):
        # an array where each index is an array of typles (val, snap_id)
        self.arr = []
        for _ in range(length):
            # tuple of (val, snap_id)
            self.arr.append([])

        self.curr_snap_id = 0


    def set(self, index: int, val: int) -> None:
        self.arr[index].append((val, self.curr_snap_id))
        

    def snap(self) -> int:
        snap_id = self.curr_snap_id
        self.curr_snap_id += 1

        return snap_id
        

    def get(self, index: int, snap_id: int) -> int:
        # Binary search for the snap_id we need
        # We may not have all of the snap_id in values or we may have more
        # than one value for each snap_id. If there does not exist one,
        # just choose the next smaller snap_id and if there does exist one,
        # cloose the one furthest back in the array (most recent).
        values = self.arr[index]

        snap_index = bisect_right(values, snap_id, key= lambda x: x[1])
        if 0 <= snap_index - 1 < len(values):
            return values[snap_index - 1][0]
        else:
            return 0


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
