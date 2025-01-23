n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def recursion(start_coor, n):
    if n == 1:
        return grid[start_coor[0]][start_coor[1]]
    
    a = start_coor[0]
    b = start_coor[1]

    new_start_coors = [(a, b), (a, b + n//2), (a + n//2, b), (a + n//2, b + n//2)]

    arr = []
    for new_start_coor in new_start_coors:
        # print("new start coor", new_start_coor)
        arr.append(recursion(new_start_coor, n//2))
    
    # print(sorted(arr)[1])
    return sorted(arr)[1]


answer = recursion((0, 0), n)
print(answer)