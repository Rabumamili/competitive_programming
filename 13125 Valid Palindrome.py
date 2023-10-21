class Solution(object):
    def isPalindrome(self, s):
        if len(s) <= 1:
            return True
        s = ''.join(letter.lower() for letter in s if letter.isalnum())

        return s == s[::-1]
