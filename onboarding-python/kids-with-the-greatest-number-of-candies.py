class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
     

        maxi = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxi:
                result.append(True)
            else:
                result.append(False)
        return result
