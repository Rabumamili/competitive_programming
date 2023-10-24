class Solution(object):
    def characterReplacement(self, s, k):
    
        max_length = 0
        max_count = 0
        char_count = [0] * 26  # Array to store the count of each character
        start = 0

        for end in range(len(s)):
            char_count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, char_count[ord(s[end]) - ord('A')])

            if (end - start + 1) - max_count > k:
                char_count[ord(s[start]) - ord('A')] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length


 
