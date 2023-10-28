def scoreOfParentheses(s):
    score = 0  # Track the overall score
    stack = []  # Track the score at each level
    for char in s:
        if char == '(':
            stack.append(score)
            score = 0  # Reset the score for the new level
        else:
            score += stack.pop() + max(score, 1)
    return score
