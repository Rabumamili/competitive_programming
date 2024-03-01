class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        sequences = set()
        repeated = set()

        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            if sequence in sequences:
                repeated.add(sequence)
            else:
                sequences.add(sequence)

        return list(repeated)