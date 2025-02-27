n = int(input())

dp = [0] * (n+1)

for i in range(2, n+1):
    t = dp[i - 1] + 1
    if i % 3 == 0:
        t = min(t, dp[i // 3] + 1)
    if i % 2 == 0:
        t = min(t, dp[i // 2] + 1)
    
    dp[i] = t

print(dp[n])