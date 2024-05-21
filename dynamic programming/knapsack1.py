
def knapsack(n, w, items):
    dp = [[0] * (w + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i-1]
        for w in range(w + 1):
            if w >= weight:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][w]


n, w = list(map(int, input().split()))
items = []
for _ in range(n):
    weights, value = list(map(int, input().split()))
    items .append((weights, value))
result = knapsack(n, w, items)
print(result)
