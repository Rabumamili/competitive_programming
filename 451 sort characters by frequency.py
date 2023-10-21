class Solution:
    def frequencySort(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        sorted_chars = sorted(freq, key=lambda x: freq[x], reverse=True)

        sorted_string = ''
        for char in sorted_chars:
            sorted_string += char * freq[char]

        return sorted_string
