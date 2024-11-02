def binarySearch(array, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if array[mid] == target:
        return mid

    elif array[mid] > target:
        binarySearch(array, target, start, mid-1)
    
    else:
        binarySearch(array, target, mid+1, end)