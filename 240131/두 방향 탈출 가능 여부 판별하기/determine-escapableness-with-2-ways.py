n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def in_range(x, y) :
    return 0<=x<n and 0<=y<m

def can_go(x,y) :
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0 :
        return False

    return True

def dfs(x, y) :
    global order
    
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys) :
        next_x, next_y = x+dx, y+dy

        if can_go(next_x, next_y) :
            visited[next_x][next_y] = 1
            dfs(next_x,next_y)


visited[0][0] = 1
dfs(0, 0)

print(visited[n-1][m-1])