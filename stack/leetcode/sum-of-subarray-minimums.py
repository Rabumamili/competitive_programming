class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        prev = [-1] * n
        nexts = [n] * n
        stack = []

        # Calculate the previous smaller  
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)

        stack = []

        # Calculate the next smaller element for each element
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:   
                stack.pop()
            if stack:
                nexts[i] = stack[-1]
            stack.append(i)

        result = 0

        # Calculate the contribution of each element to the sum
        for i in range(n):
            result = (result + arr[i] * (i - prev[i]) * (nexts[i] - i)) % MOD

        return result

 