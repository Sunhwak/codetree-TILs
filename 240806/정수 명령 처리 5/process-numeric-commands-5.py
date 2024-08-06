listA = []
n = int(input())

for _ in range(n) :
    order_k = input().split()
    order = order_k[0]

    if order == 'push_back' :
        k = order_k[1]
        listA.append(k)

    elif order == 'pop_back' :
        listA.pop()

    elif order == 'size' :
        print(len(listA))

    else :
        k = order_k[1]     
        print(listA[int(k)-1])