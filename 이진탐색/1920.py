import sys
n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline.split())))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def binarySearch(array, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if array[mid] == target:
        return True

    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    
    else:
        return binarySearch(array, target, mid+1, end)
    
for i in range(m):
    if binarySearch(cards, nums[i], 0, len(cards)-1):
        print(1, end=' ')
    else:
        print(0, end=' ')