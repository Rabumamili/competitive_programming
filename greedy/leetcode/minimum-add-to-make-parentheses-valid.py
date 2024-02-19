class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for char in s:
            if char=="(":
                stack.append(char)
            if char ==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(char)
        return len(stack)