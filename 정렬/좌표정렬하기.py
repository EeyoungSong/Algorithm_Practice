n = int(input())

arr = []
for i in range(n):
    t = tuple(map(int, input().split()))
    arr.append(t)

arr.sort()

for i in arr:
    print(i[0], i[1])