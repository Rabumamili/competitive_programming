class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                else:
                     
                    result = int(operand1 / operand2) if operand1 * operand2 >= 0 else -int(abs(operand1) / abs(operand2))

                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


