import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    elem = input().rstrip()
    arr.append(elem)

cnt = 0
for _ in range(m):
    elem = input().rstrip()
    if elem in arr:
        cnt += 1

print(cnt)