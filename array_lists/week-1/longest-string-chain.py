class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        
        for word in words:
            dp[word] = 1
            
            # Find all possible predecessors of the current word
            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
        
        return max(dp.values())