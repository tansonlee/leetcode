class Cell:
    def __init__(self, t, val):
        # Type can be "num" or "formula"
        self.type = t
        self.val = val
    
    def __repr__(self):
        return f"[{self.type}] {self.val}"

class Excel:

    def __init__(self, height: int, width: str):
        row_col = self.convert_row_col(height, width)
        self.width = row_col[1] + 1
        self.height = row_col[0] + 1
        self.sheet = [[Cell("num", 0) for _ in range(self.width)] for _ in range(self.height)]
        

    def set(self, row: int, column: str, val: int) -> None:
        row, col = self.convert_row_col(row, column)
        self.sheet[row][col] = Cell("num", val)

    def get(self, row: int, column: str) -> int:
        row, col = self.convert_row_col(row, column)
        cell = self.sheet[row][col]

        if cell.type == "num":
            return cell.val
        else:
            return self.eval_formula(cell.val)
        
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        my_row, col = self.convert_row_col(row, column)
        self.sheet[my_row][col] = Cell("formula", numbers)
        return self.get(row, column)
    
    def convert_row_col(self, row: int, column: str):
        return (row - 1, ord(column) - ord('A'))
    
    def eval_formula(self, formula):
        result = 0

        for f in formula:
            sums = f.split(":")

            start_row = None
            end_row = None
            start_col = None
            end_col = None

            if len(sums) == 1:
                start_row = int(sums[0][1:])
                end_row = int(sums[0][1:])
                start_col = sums[0][0]
                end_col = sums[0][0]
            else:
                start_row = int(sums[0][1:])
                end_row = int(sums[1][1:])
                start_col = sums[0][0]
                end_col = sums[1][0]
            
            for r in range(start_row, end_row + 1):
                for c in range(ord(start_col), ord(end_col) + 1):
                    result += self.get(r, chr(c))

        return result


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
