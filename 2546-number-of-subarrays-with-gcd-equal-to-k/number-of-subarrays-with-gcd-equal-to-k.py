class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, (a % b))
        count = 0
        n = len(nums)
        for i in range(n):
            num = nums[i]
            for j in range(i, n):
                num = gcd(num, nums[j])
                if num==k:
                    count += 1
        return count