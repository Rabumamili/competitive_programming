class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for char in s:
            if char!=")":
                stack += [char]
                continue 
                
            temp =[]
            while stack[-1]!="(":
                temp = temp+[stack.pop()]
            stack.pop()
            stack += temp

        return "".join(stack)