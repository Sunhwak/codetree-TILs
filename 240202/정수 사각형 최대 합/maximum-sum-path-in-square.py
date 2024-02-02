n = int(input())

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def DP():
    for i in range(n) :
        dp[0][i] = a[0][i]

    for i in range(1, n) :
        dp[i][0] = dp[i-1][0] + a[i][0]

DP()
for i in range(1, n) :
    for j in range(1, n) :
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])+ a[i][j]
        
print(dp[n-1][n-1])