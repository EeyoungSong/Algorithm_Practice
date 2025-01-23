
def recursion(s, l, r):
    global cnt
    cnt += 1
    if (l >= r):
        return 1
    elif (s[l] !=s[r]):
        return 0
    else: return recursion(s, l+1, r-1)


def is_palindrome(s):
    return recursion(s, 0, len(s) - 1)

cnt = 0
n = int(input())
for i in range(n):
    S = input()
    print(is_palindrome(S), cnt)
    cnt = 0



