class Solution(object):
     
    def findAnagrams(self, s, p):
        result = []
        p_freq = [0] * 26
        window_freq = [0] * 26

        for char in p:
            p_freq[ord(char) - ord('a')] += 1
      

        for i in range(len(s)):
            window_freq[ord(s[i]) - ord('a')] += 1

            if i >= len(p):
                window_freq[ord(s[i - len(p)]) - ord('a')] -= 1

            if window_freq == p_freq:
                result.append(i - len(p) + 1)
         
        return result
