class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans =0
        g.sort()
        s .sort()
        left =0
        right = 0
       
        while left < len(g) and right < len(s):
            if s[right] >= g[left]:
                ans += 1
                left += 1
            right += 1

        return ans