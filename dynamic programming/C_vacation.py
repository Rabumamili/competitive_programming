n = int(input())
acts = []
for _ in range(n):
    a, b, c = list(map(int, input().split()))
    acts.append([a, b, c])


dp = [[0] * 3 for _ in range(n)]
dp[0][0] = acts[0][0]
dp[0][1] = acts[0][1]
dp[0][2] = acts[0][2]
for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + acts[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + acts[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + acts[i][2]

print(max(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
