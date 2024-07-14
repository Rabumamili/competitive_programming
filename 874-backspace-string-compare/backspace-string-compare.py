class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def check(s):
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        
        final_s = check(s)
        final_t = check(t)
        return final_s == final_t