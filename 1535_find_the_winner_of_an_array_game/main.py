class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        front = 0
        wins = 0
        l = len(arr)
        if k > l:
            return max(arr)
        while True:
            if wins == k:
                return arr[front]
            
            first = arr[front]
            second = arr[(front + 1) % l]
            if first > second:
                wins += 1
                arr[front] = second
                arr[(front + 1) % l] = first
            else:
                wins = 1
                arr[front] = first
                arr[(front + 1) % l] = second
            front = (front + 1) % l



        
