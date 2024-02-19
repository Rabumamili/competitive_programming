class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        ans = list(palindrome)
        
        for i in range(len(palindrome)//2):
            if ans[i]!="a":
                ans[i]= "a"
                break
            if i==((len(palindrome)//2)-1):
                ans[-1]="b"
        return "".join(ans)