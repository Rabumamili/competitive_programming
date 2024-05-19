class Solution:
    def partition(self, s: str) -> List[List[str]]:
         
        def check(word: str) -> bool:
            return word == word[::-1]

        def dp(s: str, part: List[str], res: List[List[str]]):
            if not s:
                res.append(part.copy())
                return

            for i in range(len(s)):
                sub = s[:i+1]
                if check(sub):
                    part.append(sub)
                    dp(s[i+1:], part, res)
                    part.pop()

        res = []
        dp(s, [], res)
        return res