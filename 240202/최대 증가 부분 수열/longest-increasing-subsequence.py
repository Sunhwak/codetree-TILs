n = int(input())
dp = [1] * n
a = list(map(int, input().split()))

for i in range(1, n) :
    for j in range(i) :
        if a[j] < a[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

'''
import sys
INT_MIN = -sys.maxsize

n = int(input())
dp = [0] * (n+1)
a = [0] + list(map(int, input().split()))

def initialize() :
    for i in range(n) :
        dp[i] = INT_MIN

    dp[0] = 0

initialize()

for i in range(1, n+1) :
    for j in range(i) :
        if a[j] < a[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
'''