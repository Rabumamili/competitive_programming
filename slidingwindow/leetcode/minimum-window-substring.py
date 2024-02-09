class Solution:
    def minWindow(self, s: str, t: str) -> str:
 
      
        if not s or not t:
            return ""

        required_chars = {}
        cur_windowchars = {}
        for char in t:
            required_chars[char] = required_chars.get(char, 0) + 1

        left, right = 0, 0
        formed_chars = 0
        min_len = float('inf')
        ans = ""

        while right < len(s):
            char = s[right]
            cur_windowchars[char] = cur_windowchars.get(char, 0) + 1

            if char in required_chars and cur_windowchars[char] == required_chars[char]:
                formed_chars += 1

            while formed_chars == len(required_chars):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

                left_char = s[left]
                cur_windowchars[left_char] -= 1

                if left_char in required_chars and cur_windowchars[left_char] < required_chars[left_char]:
                    formed_chars -= 1

                left += 1

            right += 1

        return ans