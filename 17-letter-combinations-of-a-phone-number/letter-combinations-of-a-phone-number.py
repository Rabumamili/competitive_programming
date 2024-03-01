class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {'2': 'abc','3': 'def','4': 'ghi',  '5': 'jkl','6': 'mno', '7': 'pqrs', '8': 'tuv',
            '9': 'wxyz'
        }
        def backtrack(combination, next_digits):
            if not next_digits:
                ans.append(combination)
            else:
                for letter in letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        ans = []
        backtrack('', digits)
        return ans