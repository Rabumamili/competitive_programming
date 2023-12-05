class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums= ["999","888","777","666", "555","444","333","222","111","000"]
        maximum= ""
        for i in range(len(nums)) :
            if nums[i] in num:
                maximum=maximum+nums[i]
                break
        return maximum

        