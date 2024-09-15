class Solution:
   def findTheLongestSubstring(self , s: str) -> int:
       
        first_occurrence = {0: -1}  
        bitmask = 0
        max_length = 0

        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        for i, char in enumerate(s):
            # Update the bitmask if the character is a vowel
            if char in vowels:
                bitmask ^= (1 << vowels[char])

            # Check if the current bitmask has been seen before
            if bitmask in first_occurrence:
                max_length = max(max_length, i - first_occurrence[bitmask])
            else:
                first_occurrence[bitmask] = i

        return max_length
