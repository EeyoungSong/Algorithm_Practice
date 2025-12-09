# 조건
# 1 <= n <= 10000000
# 각 수는 10,000보다 작거나 같은 자연수 (이 조건 중요)
# 틀림
# 1. 메모리 초과 : 배열 -> dict로 변경 : 겹치는 건 개수로 저장  
# 2. 시간 초과 : 입력이 병목 -> sys 써야했음

# 3. 다시 메모리 초과 : print(f"{k}\n" * v, end="") -> 거대한 문자열을 만들면서 메모리 초과(300만개일 때)

from collections import defaultdict
import sys

input = sys.stdin.readline

dic = defaultdict(int)
for i in range(n):
    dic[int(input())] += 1

for k, v in sorted(dic.items()):
    print(f"{k}\n" * v, end="")


# -> counting sort를 써야함 
import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

cnt = [0] * 10001

for i in range(n):
    cnt[int(input())] += 1

for i in range(10001):
    if cnt[i]:
        write((str(i) + '\n') * cnt[i])

# 출력 시 메모리 더 줄이는 법
for i in range(10001):
    c = cnt[i]
    if c == 0:
        continue

    s = str(i) + '\n'

    # chunked output
    while c > 10000:  # 숫자는 원하는 대로 조절
        write(s * 10000)
        c -= 10000

    # 나머지 출력
    if c > 0:
        write(s * c)