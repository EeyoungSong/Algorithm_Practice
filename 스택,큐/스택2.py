'''
1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
'''
import sys
input = sys.stdin.readline

n = int(input())
st = []
for _ in range(n):
    s = input()
    x = s.split()[0]
    length = len(st)
    if x == "1":
        n = s.split()[1]
        st.append(n)
    elif x == "2":
        print(st.pop() if length > 0 else -1)
    elif x == "3":
        print(length)
    elif x == "4":
        print(1 if length == 0 else 0)
    else:
        print(st[-1] if length > 0 else -1)



