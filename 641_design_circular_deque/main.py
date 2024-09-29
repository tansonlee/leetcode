class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.front = 0 # where to place the next front element
        self.back = 1 % k # where to place the next end element
        self.k = k
        self.num_elements = 0
        
    
    def next_idx(self, idx):
        return (idx + 1) % self.k
    

    def prev_idx(self, idx):
        return (idx - 1) % self.k


    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.arr[self.front] = value
        self.front = self.prev_idx(self.front)
        self.num_elements += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.arr[self.back] = value
        self.back = self.next_idx(self.back)
        self.num_elements += 1
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.front = self.next_idx(self.front)
        self.num_elements -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.back = self.prev_idx(self.back)
        self.num_elements -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        index = self.next_idx(self.front)
        return self.arr[index]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        index = self.prev_idx(self.back)
        return self.arr[index]
        

    def isEmpty(self) -> bool:
        return self.num_elements == 0
        

    def isFull(self) -> bool:
        return self.num_elements == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
