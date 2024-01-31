n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(m)
]

answer = [ 
    [0 for _ in range(n)]
    for _ in range(m)
]

visited = [
    [False for _ in range(n)]
    for _ in range(m)
]

order = 1


def in_range(x, y):
    return 0<=x<n and 0<=y<m

def can_go(x,y) :
    if not in_range(x,y) :
        return False
    if visited[x][y] or grid[x][y] == 0 :
        return False
    return True

def push(x, y) :
    global order

    answer[x][y] = order
    order += 1
    visited[x][y] = True
    q.append(x, y)

def bfs(x, y) :
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    while q :
        x, y = q.popleft()

    for dx, dy in zip(dxs, dys) :
        next_x, next_y = x+dx, y+dy
        if can_go(next_x, next_y) :
            push(next_x, next_y)


    x, y