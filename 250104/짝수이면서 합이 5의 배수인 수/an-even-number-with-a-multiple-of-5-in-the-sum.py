def YesOrNo(x) :
    ten = x // 10
    one = x % 10
    if x % 2 == 0 and (ten+one) % 5 == 0 :
        return 'Yes'

    else : 
        return 'No'

n = int(input())
print(YesOrNo(n))