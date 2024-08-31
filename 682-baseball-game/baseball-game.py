class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == 'C':
                stack.pop()
            elif operations[i] == 'D':
                stack.append(stack[-1] * 2)
            elif operations[i] == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(operations[i]))
        return sum(stack)

        