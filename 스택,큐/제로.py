import sys
input = sys.stdin.readline

k = int(input())
st = []

for _ in range(k):
    n = int(input())
    if n != 0:
        st.append(n)
    else:
        st.pop()

print(sum(st))