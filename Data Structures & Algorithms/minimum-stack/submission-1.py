class MinStack:

    def __init__(self):
        self.stck=[]
        self.minstck=[]

    def push(self, val: int) -> None:
        self.stck.append(val)
        if not self.minstck or val <= self.minstck[-1]:
            self.minstck.append(val)

    def pop(self) -> None:
        if self.stck[-1] == self.minstck[-1]:
            self.minstck.pop()
        self.stck.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.minstck[-1]
