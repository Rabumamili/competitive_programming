class Solution:
     
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def backtrack(idx):
            nonlocal ans
            if idx==len(cookies):
                ans= min(ans, max(split))
                return
            # give to a new kid
            if len(split)<k:
                split.append(cookies[idx])
                backtrack(idx+1)
                split.pop()
            # give to a kid that already has cookies
            for i in range(len(split)):
                if split[i]+cookies[idx] < ans:
                    split[i] += cookies[idx]
                    backtrack(idx+1)
                    split[i] -= cookies[idx]
            

        split = []
        ans = float("inf")
        backtrack(0)
        return ans
    
        

 
            