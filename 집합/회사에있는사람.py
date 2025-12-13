import sys
input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    s, exist = input().split()
    dic[s] = 1 if exist == "enter" else 0

for k, v in sorted(dic.items(), reverse=True):
    if v == 1:
        print(k)

