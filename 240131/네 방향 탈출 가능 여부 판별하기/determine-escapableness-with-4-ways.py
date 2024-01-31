'''
from collections import deque

n, m = map(int, input().split())

a = [list(map(int, input().split()))for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y) :
    return 0<=x<n and 0<=y<m

def bfs() :
    while q :
        r, c = q.popleft() # 현재 위치가 r행 c열을 탐색 중이다.
        dxs = [-1, 1, 0, 0]
        dys = [0, 0, -1, 1]

        for dx, dy in zip(dxs, dys) :
            next_x, next_y = r+dx, c+dy
            if in_range(next_x, next_y) and a[next_x][next_y] == 1 and not visited[next_x][next_y] :
                visited[next_x][next_y] = 1
                q.append((next_x, next_y))

q = deque()
visited[0][0] = 1
q.append((0,0))

bfs()
print(visited[n-1][m-1])
'''

from collections import deque

n, m = map(int, input().split())

a = [
    list(map(int, input().split()))
    for _ in range(m)
]

a[n-1][m-1] = 'x'



def can_go(x, y) :
    if x<0 and x<=n and y<0 and y<=m :
        return False
    else :
        return a[x][y] == 1 or a[x][y] == 'x'

q = deque()
def bfs() : 
    while q :
        x, y = q.popleft()

        if a[x][y] == 'x' :
            return 1
    
        else :
            a[x][y] = '.'
            dxs = [-1, 1, 0, 0]
            dys = [0, 0, -1, 1]
            for dx, dy in zip(dxs, dys) :
                if can_go(x+dx, y+dy) :
                    q.append((x+dx, y+dy))
    return 0

q.append((0,0))

print(bfs())