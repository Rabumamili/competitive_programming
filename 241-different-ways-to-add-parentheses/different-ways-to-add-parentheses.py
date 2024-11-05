class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def solve(s):
            if s in memo:
                return memo[s]
            
            results = []
            n = len(s)
            for i in range(n):
                if s[i] in "+-*":
                    left = solve(s[:i])
                    right = solve(s[i + 1:])
                   
                    for l in left:
                        for r in right:
                            if s[i] == '+':
                                results.append(l + r)
                            elif s[i] == '-':
                                results.append(l - r)
                            elif s[i] == '*':
                                results.append(l * r)
            
            if not results:
                results.append(int(s))
         
            memo[s] = results
            return results
        
        return solve(expression)