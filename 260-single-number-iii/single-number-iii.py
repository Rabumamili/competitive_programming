class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for n in nums:
            xor ^= n
        
        rightmost = xor & -xor
        
        num1, num2 = 0, 0
        for n in nums:
            if n & rightmost:
                num1 ^= n
            else:
                num2 ^= n
        
        return [num1, num2]