# 정사각형 4개로 나눠 -> 두번째로 큰 숫자 뽑기
# N은 2^n 임 


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


# 1, 1 ~ 2, 2 / 1, 1 ~ n/2, n/2 
# 1, 3 ~ 2, 4 / 1, n/2 + 1 ~ n/2, n
# 3, 1 ~ 4, 2 / n/2 + 1, 1 ~ n, n/2
# 3, 3 ~ 4, 4 / n/2 + 1, n, n




target_arr = []

def recursion(n):
    if n / 2 < 1:
        return grid
    
    a = 1 
    b = n/2 
    c = n/2 + 1
    d = n

    partition = [[(a, b), (b, b)], [(a, c), (b, d)], [(c, a), (d, b)], [(c, c), (d, d)]]

    
    for arr in partition:
        for i in range(arr[0][0], arr[0][1]):
            for j in range(arr[1][0], arr[1][1]):
                print(i, j)
                # target_arr.append(grid[i][j])
                recursion(n/2)


    target_arr.sort()
    return target_arr[1]
                


