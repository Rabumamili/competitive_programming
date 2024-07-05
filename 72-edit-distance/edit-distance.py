class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i, j):
            # If one of the strings is empty, return the length of the other  
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
            else:
                insert_op = 1 + dp(i, j + 1)     
                delete_op = 1 + dp(i + 1, j)     
                replace_op = 1 + dp(i + 1, j + 1) 
                memo[(i, j)] = min(insert_op, delete_op, replace_op)

            return memo[(i, j)]

        return dp(0, 0)