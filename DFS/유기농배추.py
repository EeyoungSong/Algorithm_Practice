import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가 안해서 런타임 에러 남

def dfs(r, c):
    global visited

    if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0 or visited[r][c] == 1:
        return 

    visited[r][c] = 1

    drs = [1, 0, -1, 0]
    dcs = [0, 1, 0, -1]
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        dfs(nr, nc)
        
T = int(input())
cnt = 0
for _ in range(T):
    m, n, k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    k_arr = []
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        j, i = map(int, input().split())
        grid[i][j] = 1
        k_arr.append((i,j))

    for r, c in k_arr:
        if  visited[r][c] != 1:
            dfs_cnt = 0
            dfs(r, c)
            cnt += 1
    print(cnt)
    cnt = 0







