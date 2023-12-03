class Solution(object):
    def maxVowels(self, s, k):
        maxVowels= 0
        count=0
        for i,x in enumerate(s):
            if x in "aeiou":
                count+=1

            if i>=k and s[i-k] in "aeiou":
                count-=1

            maxVowels=max(maxVowels,count)

        return maxVowels

        