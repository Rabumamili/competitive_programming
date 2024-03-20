class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
         
         
        ans = sorted(freq, key= lambda x: (-freq[x],x))
        return ans[:k]