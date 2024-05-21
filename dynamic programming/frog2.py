def mincost(n, k, heights):
    dp = [float('inf')] * n
    dp[0] = 0

    for i in range(n):
        for j in range(1, k + 1):
            if i + j < n:
                dp[i + j] = min(dp[i + j], dp[i] +
                                abs(heights[i] - heights[i + j]))
    return dp[n - 1]


n, k = map(int, input().split())
heights = list(map(int, input().split()))
print(mincost(n, k, heights))
