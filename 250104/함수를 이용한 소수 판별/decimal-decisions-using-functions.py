a, b = map(int, input().split())

prime_total = 0 

def is_prime(n) :
    for i in range(n-1, 0, -1) :
        if i == 1 :
            return True
            
        if n % i == 0 :
            return False

for j in range(a, b+1) :
    if is_prime(j) :
        prime_total += j

print(prime_total)