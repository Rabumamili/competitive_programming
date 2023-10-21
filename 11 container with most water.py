class Solution(object):
    def maxArea(self, height):
        ln = 0
        r = len(height)-1

        maxWater = 0

        while r > ln:

            if height[ln] < height[r]:
                maxWater = max(maxWater, height[ln] * (r-ln))
                ln += 1
            else:
                maxWater = max(maxWater, height[r] * (r-ln))
                r -= 1
        return maxWater
