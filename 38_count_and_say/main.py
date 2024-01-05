class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1" 

        for i in range(n - 1):
            next = ""
            ptr = 0
            while ptr < len(result):
                curr_num = result[ptr]
                # seek to the first num that is not curr_num
                moves = 0
                while ptr < len(result) and result[ptr] == curr_num:
                    ptr += 1
                    moves += 1
                next += str(moves) + curr_num
            result = next
        
        return result

        
