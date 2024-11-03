import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

card_dict = {}
for card in cards:
    if card not in card_dict:
        card_dict[card] = 1
    else:
        card_dict[card] += 1

sorted_cards = sorted(list(set(cards)))

m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def binarySearch(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2

    if arr[mid] == target:
        return True
    
    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid-1)

    else:
        return binarySearch(arr, target, mid+1, end)

for i in range(m):
    if binarySearch(sorted_cards, arr[i], 0, len(sorted_cards)-1):
        print(card_dict[arr[i]], end=" ")
    else:
        print(0, end=" ")


    
# def checkSameNumber(arr, target, idx):
#     rcnt = 0
#     lcnt = 0
#     ridx = idx
#     lidx = idx
#     while ridx < len(arr)-1:
#         ridx += 1
#         if arr[ridx] == target:
#             rcnt += 1
#         else:
#             break

#     while lidx >= 1:
#         lidx -= 1
#         if arr[lidx] == target:
#             lcnt += 1
#         else:
#             break
        
#     return rcnt + lcnt + 1



# for i in range(m):
#     idx = binarySearch(cards, arr[i], 0, len(cards)-1)
#     if idx:
#         num = checkSameNumber(cards, arr[i], idx)
#         print(num, end=" ")
#     else:
#         print(0, end=" ")


