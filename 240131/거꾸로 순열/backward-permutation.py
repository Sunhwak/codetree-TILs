n = int(input())
visited = [False] * (n+1)
answer = []

def print_answer() :
    for ele in answer :
        print(ele, end = ' ')
    print()

def pick(cnt) :
    if cnt == n+1 :
        print_answer()
        return
    
    for i in range(n, 0, -1) :
        if visited[i] :
            continue
        
        visited[i] = True
        answer.append(i)
        
        pick(cnt+1)

        answer.pop()
        visited[i] = False
    
pick(1)