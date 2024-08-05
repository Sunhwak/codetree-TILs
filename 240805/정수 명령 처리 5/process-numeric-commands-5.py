listA = []
n = int(input())

for _ in range(n):
    order = input()

    if order.startswith('push_back') :
        _, num = tuple(order.split())
        listA.append(int(num))

    elif order.startswith('pop_back') :
        listA.pop()

    elif order.startswith('size') :
        print(len(listA))

    else :
        _, index = tuple(order.split())
        print(listA[int(index)-1])