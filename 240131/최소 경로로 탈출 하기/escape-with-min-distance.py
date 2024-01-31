from collections import deque

n, m = map(int, input().split())

# 지도 입력
a = [list(map(int, input().split())) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]  # 각 정점을 방문했는 지 여부
dist = [[-1 for _ in range(m)] for _ in range(n)]    # dist[i][j] := (i, j)에 도달하는 데에 필요한 최소 이동 횟수


def bfs():
    # q를 가지고 너비 우선 탐색
    while q:
        r, c = q.popleft()  # 현재 위치가 r행 c열을 탐색 중이다.

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc  # (r, c) 와 인접한 칸인 (nr, nc) 찾기

               # 격자를 벗어나지 않는 지       / 뱀이 없는 지    /  방문한 적이 없는 ㅈㅣ 
            if 0 <= nr < n and 0 <= nc < m and a[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))




q = deque()  # 새로운 queue 를 생성
visited[0][0] = 1  # (0, 0)은 탐색 성공
dist[0][0] = 0     # (0, 0)까지는 거리가 0 이다.
q.append((0, 0))   # (0, 0)은 탐색 가능하다고 queue에 추가하기

bfs()  # 탐색 수행

print(dist[n - 1][m - 1])