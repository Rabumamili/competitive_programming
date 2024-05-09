class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = happiness[0]
        i = 1
        while k > 1 and i < len(happiness):
            
            if happiness[i]-i > 0:
                ans += happiness[i]-i
            k -= 1
            i += 1
        return ans
