a, b = map(int, input().split())

cnt = 0

def is_369(n) :
    n = str(n)
    for ele in n :
        if ele in '369' :
            return True

def is_multiple(n) :
    return n % 3 == 0

for i in range(a, b+1) :
    if is_369(i) or is_multiple(i) :
        cnt += 1

print(cnt)