import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for i in range(1, n+1):
    s = input().strip()
    dic[str(i)] = s
    dic[s] = i


for _ in range(m):
    print(dic[input().strip()])