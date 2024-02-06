n = int(input())

def calc(num) :
    sum_all = 0
    for i in range(n, 0, -1) :
        sum_all += i
          
    sum_all = sum_all // 10
    return sum_all

print(calc(n))