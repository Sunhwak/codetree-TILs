n = int(input())

dp = [0] * (n+1)

if n >= 2 :
    dp[1] = 1
    dp[2] = 1
else :
    dp[1] = 1

for i in range(3, n+1) :
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])


'''
n = 6
memo = [-1] * (n+1)

def fib(n) :
    if memo[n] != -1 :
        return memo[n]

    if n<=2:
        memo[n] = 1
    else:
        memo[n] = fib(n-1) + fib(n-2)

    return memo[n]
'''