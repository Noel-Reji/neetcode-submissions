class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sumarr = []

        for i in operations:
            if i == "C":
                sumarr.pop()

            elif i == "D":
                x = sumarr[-1]
                sumarr.append(x * 2)

            elif i == "+":
                x = sumarr[-1]
                y = sumarr[-2]
                sumarr.append(x + y)

            else:
                sumarr.append(int(i))

        return sum(sumarr)