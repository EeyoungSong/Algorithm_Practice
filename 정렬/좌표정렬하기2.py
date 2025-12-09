# 방법 1
n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))

arr.sort()

for i in arr:
    print(i[1], i[0])

# 방법 2 (lambda)

n = int(input())

arr = []
for i in range(n):
    t = tuple(map(int, input().split()))
    arr.append(t)

arr.sort(key=lambda x: (x[1], x[0]))

for i in arr:
    print(i[0], i[1])


