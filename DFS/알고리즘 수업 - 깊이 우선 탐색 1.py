import sys
sys.setrecursionlimit(10**9)

n, m, r = map(int, sys.stdin.readline().split())


grid = [[] for _ in range(n+1)]
visited = set()
order_arr = [0] * (n)
order = 1


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    grid[a].append(b)
    grid[b].append(a)

for arr in grid:
    arr.sort()

def dfs(node):
    global order

    visited.add(node)
    order_arr[node-1] = order
    order += 1

    for next_node in grid[node]:
        if next_node not in visited:
            dfs(next_node) 

visited.add(r)
order_arr[r-1] = order
order += 1
for node in grid[r]:
    if node not in visited:
        dfs(node)


for item in order_arr:
    print(item)

