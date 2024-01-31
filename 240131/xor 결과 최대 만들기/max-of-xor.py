import functools

n, m = map(int, input().split())
a = list(map(int, input().split()))
visited = [
    False for _ in range(n)
]
ans = 0

def xor():
    val = 0
    for i in range(n) :
        if visited[i]:
            val ^= a[i]
    return val
        
def find_max_xor(curr_idx, cnt) :
    global ans
    
    if cnt == m :
        ans = max(ans, xor())
        return

    if curr_idx == n :
        return

    find_max_xor(curr_idx+1, cnt)

    visited[curr_idx] = True
    find_max_xor(curr_idx+1, cnt+1)
    visited[curr_idx] = False

find_max_xor(0, 0)
print(ans)