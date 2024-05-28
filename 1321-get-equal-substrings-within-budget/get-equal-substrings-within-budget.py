class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
   
        n = len(s)
        left = 0
        max_length = 0
        curcost = 0

        for right in range(n) :
            cost = abs(ord(s[right]) - ord(t[right]))
            curcost += cost

            while curcost > maxCost:
                curcost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
             

        return max_length

    