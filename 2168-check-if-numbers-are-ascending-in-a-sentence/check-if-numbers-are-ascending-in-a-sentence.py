class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split()
        maxnum = -1
        for word in words:
            if word.isdigit():
                if int(word) > maxnum:
                    maxnum = int(word)
                else:
                    return False
        return True


