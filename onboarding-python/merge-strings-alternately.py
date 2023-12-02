class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        strng=""
        if len(word1)>len(word2):
            target=word1
        else:
            target=word2            
        a=min(len(word1),len(word2))
        for i in range(a):
            strng+=word1[i]
            strng+=word2[i]
        strng+=target[a:]
        return strng
            





        