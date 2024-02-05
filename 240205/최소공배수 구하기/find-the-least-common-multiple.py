n, m = map(int, input().split())

def max_gong(n, m) :
    for i in range(min(n, m), 0, -1) :
        if n%i==0 and m%i==0 :
            gong = (n//i) * (m//i) * i
            print(gong)
            break

max_gong(n, m)