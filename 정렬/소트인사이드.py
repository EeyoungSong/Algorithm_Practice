from collections import defaultdict

dic = defaultdict(int)
for i in list(map(int, input())):
    dic[i] += 1

for k, v in reversed(sorted(dic.items())):
    print(f"{k}" * v, end="")