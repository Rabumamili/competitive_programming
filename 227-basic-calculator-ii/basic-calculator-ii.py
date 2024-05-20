class Solution:
    def calculate(self, s: str) -> int:
 
        if not s:
            return 0

        stk = []
        num = 0
        op = '+'
        n = len(s)

        for i in range(n):
            ch = s[i]

            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in "+-*/" or i == n - 1:
                if op == '+':
                    stk.append(num)
                elif op == '-':
                    stk.append(-num)
                elif op == '*':
                    stk.append(stk.pop() * num)
                elif op == '/':
                    stk.append(int(stk.pop() / num))

                op = ch
                num = 0

        return sum(stk)

    
