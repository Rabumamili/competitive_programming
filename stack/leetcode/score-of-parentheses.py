class Solution(object):
    def scoreOfParentheses(self, s):
     
        score = 0   
        stack = []  # Track the score at each level
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0  # Reset the score for the new level
            else:
                score += stack.pop() + max(score, 1)
        return score