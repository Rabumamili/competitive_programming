class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        # Calculate the prefix sums for even and odd indices
        evensum = [0] * (n + 1)
        oddsum = [0] * (n + 1)

        for i in range(n):
         
            if i % 2 == 0:
                evensum[i + 1] = evensum[i] + nums[i]           
            else:
                evensum[i + 1]  = evensum[i]
            if i %2 ==1: 
                oddsum[i + 1] = oddsum[i] + nums[i]  
            else:
                oddsum[i + 1]= oddsum[i] 


        # check if removing that index makes the array fair
        for i in range(n):
            new_even_sum = evensum[i] + oddsum[n] - oddsum[i + 1]
            new_odd_sum = oddsum[i] + evensum[n] - evensum[i + 1]

            if new_even_sum == new_odd_sum:
                count += 1

        return count

    