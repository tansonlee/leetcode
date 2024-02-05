class TextEditor:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def addText(self, text: str) -> None:
        for char in text:
            self.s1.append(char)

    def deleteText(self, k: int) -> int:
        result = 0
        for i in range(k):
            if len(self.s1) == 0:
                break
            self.s1.pop()
            result += 1
        return result

    def cursorLeft(self, k: int) -> str:
        for i in range(k):
            if len(self.s1) == 0:
                break
            self.s2.append(self.s1.pop())
        
        return "".join(self.s1[-min(10, len(self.s1)):])

    def cursorRight(self, k: int) -> str:
        for i in range(k):
            if len(self.s2) == 0:
                break
            self.s1.append(self.s2.pop())
        
        return "".join(self.s1[-min(10, len(self.s1)):])
        
# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
