n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
pieces = [1 for _ in range(k)]

ans = 0

def find_max_horse(cnt) :
    global ans 
    ans = max(ans, count_horse())

    if cnt == n :
        return

    for i in range(k):
        if pieces[i] >= m :
            continue

        pieces[i] += nums[cnt]
        find_max_horse(cnt+1)
        pieces[i] -= nums[cnt]

def count_horse() :
    score = 0
    for piece in pieces :
        score += (piece >= m)

    return score


find_max_horse(0)
print(ans)


'''
n, m, k = map(int, input().split())
route = [0] +list(map(int, input().split()))
final = [[0] * (m+1) for _ in range(k)]
for i in range(k) :
    final[i][1] = 1

max_cnt = -1
def print_max(cnt):
    if cnt > max_cnt :
        max_cnt = cnt
    return max_cnt

def count_play() :
    cnt = 0
    for i in range(k) :
        cnt += final[i][-1]

    return cnt

def go(num):
    if num == n :
        cnt = count_play()
        print_max()
        return
    
    for i in route[1:] :
'''