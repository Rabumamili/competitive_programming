class Solution:
    def sortSentence(self, s: str) -> str:
        
        words = s.split()  
        wordsidx = [(word[:-1], int(word[-1])) for word in words]   
        wordsidx.sort(key=lambda x: x[1])   
        sentence = ' '.join([word[0] for word in wordsidx])   
        return  sentence