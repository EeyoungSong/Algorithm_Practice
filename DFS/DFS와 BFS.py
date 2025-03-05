import sys
sys.setrecursionlimit(10**6)

n, m, v = map(int, sys.stdin.readline().split())

def dfs(node):
    dfs_visited.add(node)
    print(node, end=" ")

    for next_node in linked_list[node]:
        if next_node not in dfs_visited:
            dfs(next_node)

def bfs():
    if len(queue) <= 0:
        return
    
    # print("queue", queue)
    # print("bfs_visited", bfs_visited)
    node = queue.pop(0)  
    print(node, end=" ")
    for next_node in linked_list[node]:
        if next_node not in bfs_visited:
            queue.append(next_node)
            bfs_visited.append(next_node)
    bfs()

linked_list = [[] for _ in range(n+1)] # 연결 리스트로 그래프 받기 

# dfs 실행
dfs_visited = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    linked_list[a].append(b)
    linked_list[b].append(a)

for arr in linked_list:
    arr.sort()
dfs_visited.add(v)
dfs(v)
print()

# bfs 실행
bfs_visited = []
queue = []
queue.append(v)
bfs_visited.append(v)
bfs()
