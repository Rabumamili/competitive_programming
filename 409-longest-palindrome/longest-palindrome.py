class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        char_count={}
        for char in s:
            char_count[char]= char_count.get(char,0) + 1
            
        final= 0
        odd_found= False

        for char in char_count:
            if char_count[char]%2 == 0:
                final +=char_count[char]
            else:
                final += (char_count[char] -1)
                odd_found = True
        if odd_found: 
            final += 1

        return final

