class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
 
        max_score, max_count = 0, 0
        left = 0
        counts = {'T': 0, 'F': 0}

        for right, element in enumerate(answerKey):
            counts[element] += 1
            max_count = max(max_count, max(counts['T'], counts['F']))

            if right - left + 1 - max_count > k:
                counts[answerKey[left]] -= 1
                left += 1

            max_score = max(max_score, right - left + 1)

        return max_score
