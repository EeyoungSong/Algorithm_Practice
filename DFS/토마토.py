from collections import deque

m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
starts = [(r, c) for c in range(len(grid[0])) for r in range(len(grid)) if grid[r][c] == 1]

queue = deque([start for start in starts])

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs():
    max_num = 0
    while len(queue) > 0:
        r, c = queue.popleft()
        drs, dcs = [0, 1, 0, -1], [1, 0, -1, 0]
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if in_range(nr, nc) and not visited[nr][nc] and grid[nr][nc] == 0:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                max_num = max(max_num, visited[nr][nc])
                
    return max_num


ans = bfs()
print(visited)
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0 and visited[i][j] == 0:
            ans = -1
print(ans)



