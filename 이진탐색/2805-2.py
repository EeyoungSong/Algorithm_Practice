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
    elif i == 0:
        idx_arr.append(idx_arr[n-2-i] + (arr[i]) * (n-i))
    else:
        idx_arr.append(idx_arr[n-2-i] + (arr[i] - arr[i-1]) * (n-i))

idx_arr.insert(0, 0)

search = binarySearch(idx_arr, m, 0, len(idx_arr)-1)
cur_diff = search
print(search)
end_num = idx_arr[search]
start_num = idx_arr[search - 1]

cnt = (m - start_num) // cur_diff
print("idx_arr", idx_arr)
print(search, cur_diff, end_num, start_num, cnt)

for i in range(1, search):
    cnt += (idx_arr[i] - idx_arr[i-1]) // (i)

if (m - start_num) % cur_diff == 0:
    print(arr[-1] - cnt)
else:
    print(arr[-1] - (cnt + 1))


