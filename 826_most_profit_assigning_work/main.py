class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_and_profit = sorted([(profit[i], difficulty[i]) for i in range(len(difficulty))])
        worker.sort()

        dp_ptr = len(difficulty_and_profit) - 1
        w_ptr = len(worker) - 1

        result = 0
        while dp_ptr >= 0 and w_ptr >= 0:
            if worker[w_ptr] >= difficulty_and_profit[dp_ptr][1]:
                result += difficulty_and_profit[dp_ptr][0]
                w_ptr -= 1
            else:
                dp_ptr -= 1
        return result
        
