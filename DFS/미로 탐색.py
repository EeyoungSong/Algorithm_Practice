import sys
from collections import deque

sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs():
    global answer

    r, c, cnt = queue.popleft()

    if r == n-1 and c == m-1:
        answer = cnt
        return

    drs, dcs = [1, 0, -1, 0], [0, 1, 0, -1]

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and grid[nr][nc] != 0 and bfs_visited[nr][nc] != 1:
            queue.append((nr, nc, cnt+1))
            bfs_visited[nr][nc] = 1

    bfs()



# bfs 실행
answer = -1
bfs_visited = [[0] * m for _ in range(n)]
queue = deque()
queue.append((0, 0, 1)) 
bfs_visited[0][0] = 1
bfs()

print(answer)


# 트리의 깊이를 어떻게 기록하지?
# 