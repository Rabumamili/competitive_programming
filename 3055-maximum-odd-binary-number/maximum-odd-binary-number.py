class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s)==1:
            return s
        nums = [i for i in s]
        nums.sort(reverse= True)
        if nums[-1]!="1":
            right = len(s)-2
            while right >-1:
                if nums[right] =="1":
                    nums[right], nums[-1]= nums[-1], nums[right]
                    break
                right -=1

        
        return "".join(nums)
        