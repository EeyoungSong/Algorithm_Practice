# 나무 M 미터, 나무 수 n개
# 절단기 높이 H -> 연속해서 자름 H보다 크면 잘림
# 필요한 만큼만 가져갈 것
# 적어도 M미터를 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값

# 1트 - 메모리 초과

import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

def binarySearch(arr, target, start, end):
    if start > end:
        return start
    
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid-1)
    else:
        return binarySearch(arr, target, mid+1, end)


idx_arr = []
for i in range(n-1, -1, -1):
    if i == n-1:
        idx_arr.append(arr[i] - arr[i-1])
        print(arr[i], arr[i-1], idx_arr)
    elif i == 0:
        idx_arr.append(idx_arr[n-2-i] + (arr[i]) * (n-i))
    else:
        idx_arr.append(idx_arr[n-2-i] + (arr[i] - arr[i-1]) * (n-i))



add_num = 1
cur_idx = 1
cnt = 0
while add_num < idx_arr[-1]:
    add_num += cur_idx
    cnt += 1
    if add_num == m:
        print(arr[-1] - cnt)
        break

    elif add_num > m:
        print(arr[-1] - cnt)
        break

    if idx_arr[cur_idx-1] == add_num:
        cur_idx += 1

# print(arr[-1] - (binarySearch(num_arr, m, 0, len(num_arr)-1)+1))

