class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total  

        for i, chal in enumerate(chalk):
            if k < chal:
                return i
            k -= chal