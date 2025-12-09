import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    age, name = input().split()
    age = int(age)
    
    if age not in dic:
        dic[age] = [name]
    else:
        dic[age].append(name)

for k, v in sorted(dic.items()):
    for elem in v:
        print(f"{k} {elem}")

