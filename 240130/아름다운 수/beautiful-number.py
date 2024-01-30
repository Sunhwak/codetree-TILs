n = int(input())
ans = 0
seq = []

def beautiful_num() :
    i = 0
    while i < n :
        if i + seq[i] -1 >= n :
            return False

        for j in range(i, i+seq[i]) :
            if seq[j] != seq[i] :
                return False
        i += seq[i]

    return True

def count_beatiful_num(cnt) :
    global ans
    if cnt == n :
        if beautiful_num() :
            ans += 1
        return
    for i in range(1, 5) :
        seq.append(i)
        count_beatiful_num(cnt+1)
        seq.pop()

count_beatiful_num(0)
print(ans)