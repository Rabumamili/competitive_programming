class Solution(object):
    def maxTurbulenceSize(self, arr):

        n = len(arr)
        if n < 2:
            return n

        max_length = 1
        up = down = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = down = 1

            max_length = max(max_length, max(up, down))

        return max_length
