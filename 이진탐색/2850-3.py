# 나무 M 미터, 나무 수 n개
# 절단기 높이 H -> 연속해서 자름 H보다 크면 잘림
# 필요한 만큼만 가져갈 것
# 적어도 M미터를 가져가기 위해 절단기에 설정할 수 있는 높이의 최대값

# 1트 - 메모리 초과

import sys
n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))

    
def cal_cur(mid):
    s = 0
    for a in arr:
        if a > mid:
            s += a - mid 
    return s

def binarySearch(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        cur = cal_cur(mid)

        if cur == target:
            return mid
        
        elif cur > target:
            start = mid + 1
        
        else:
            end = mid - 1
    
    return end


print(binarySearch(arr, m, 0, max(arr)-1))



