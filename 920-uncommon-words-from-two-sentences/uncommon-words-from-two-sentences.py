class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Concatenate the two sentences with a space in between
        sentence = s1 + " " + s2

        # Dictionary to store word frequency
        word_count = defaultdict(int)
        words = sentence.split()

        # Count occurrences of each word
        for word in words:
            word_count[word] += 1

        # List to store words that appear exactly once
        result = [word for word in word_count if word_count[word] == 1]

        return result