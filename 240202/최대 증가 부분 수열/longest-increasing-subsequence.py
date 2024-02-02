import sys
INT_MIN = -sys.maxsize

n = int(input())
dp = [0] * n
a = list(map(int, input().split()))

def initialize() :
    for i in range(n) :
        dp[i] = INT_MIN

    dp[0] = 0

initialize()

for i in range(1, n) :
    for j in range(0, i) :
        if dp[j] == INT_MIN :
            continue
        
        if a[j] < a[i] :
            dp[i] = max(dp[i], dp[j]+1)

ans = 0
for i in range(n) :
    ans = max(ans, dp[i])

print(ans+1)