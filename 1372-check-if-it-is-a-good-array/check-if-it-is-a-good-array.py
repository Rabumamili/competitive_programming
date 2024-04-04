class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if gcd(*nums)==1:
            return True
        return False