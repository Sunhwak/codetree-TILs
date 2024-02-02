n = int(input())
dp = [1] * n
a = list(map(int, input().split()))

for i in range(1, n) :
    for j in range(i) :
        if a[j] > a[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))