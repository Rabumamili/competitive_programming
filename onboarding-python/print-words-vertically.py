class Solution:
    def printVertically(self, s: str) -> List[str]:

        words = s.split()
        max_length = max(len(word) for word in words)
        result = []

        for i in range(max_length):
            column = ""
            count = 0

            for word in words:
                if len(word) > i:
                    column += " " * count
                    count = 0
                    column += word[i]
                else:
                    
                    count += 1

            result.append(column)

        return result
            
            


            