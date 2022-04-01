class CQueue:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if self.stack1 == [] and self.stack2 == []:
            return -1
        elif self.stack2 == []:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(1)
obj.appendTail(2)
obj.appendTail(3)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
obj.appendTail(4)
obj.appendTail(5)
param_2 = obj.deleteHead()
print(param_2)

