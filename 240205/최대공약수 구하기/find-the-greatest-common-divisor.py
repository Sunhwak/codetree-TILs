n, m = map(int, input().split())

def max_gcd(n, m) :
    for i in range(min(n,m), 0, -1) :
        if n % i == 0 and m % i == 0 :
            gcd = i
            print(gcd)
            break
    

max_gcd(n, m)