class Solution:
    def minimumSteps(self, s: str) -> int:
        black, ans = 0, 0
        for digit in s:
            if digit =="1":
                black += 1
            else:
                ans += black
        return ans






        # count = 0
        # left = 0
        # right = len(s)-1

        # while left < right:
        #     if s[left] == "1" and s[right]=='0':
        #         count += right - left
        #         left += 1
        #         right -= 1
        #     elif s[left] == "0" and s[right] =="1":
        #         right -= 1
        #         left += 1
        #     elif s[left] == "1" and s[right] =="1":
        #         right -= 1
        #     elif s[left] == "0" and s[right] =="0":
        #         left += 1

        # return count
            
        
         





            
        

        
