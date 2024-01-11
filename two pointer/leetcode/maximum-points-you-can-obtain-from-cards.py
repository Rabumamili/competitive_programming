class Solution(object):
    def maxScore(self, cardPoints, k):
    
        l = len(cardPoints)
        min_sum = float('inf')
        cur_sum = 0 
        total = sum(cardPoints)
        sub_arr = l - k 

        left = 0 
        for right in range(l): 
            cur_sum += cardPoints[right]
            while right - left + 1 > sub_arr: 
                cur_sum -= cardPoints[left]
                left += 1

            if right - left + 1 == sub_arr: 
                min_sum = min(min_sum, cur_sum)

        return total - min_sum