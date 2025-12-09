import sys

input = sys.stdin.readline

n = int(input())
len_arr = [[] for _ in range(52)]
for i in range(n):
    s = input()
    idx = len(s)
    if s not in len_arr[idx]:
        len_arr[idx].append(s)

for arr in len_arr:
    if len(arr) > 0:
        arr.sort()
        for elem in arr:
            print(elem, end="")

