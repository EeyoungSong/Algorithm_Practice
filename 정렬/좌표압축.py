import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sorted_set_arr = list(sorted(set(arr)))
idx_dict = {elem: idx for idx, elem in enumerate(sorted_set_arr)}

print(" ".join([str(idx_dict[a]) for a in arr]))


# print(" ".join([str(sorted_set_arr.index(a)) for a in arr]))
# 위처럼 index 썼는데 시간 복잡도 1%에서 짤림 
# 그래서 dict로 바꿔서 인덱스 맵핑 미리 해줬더니 시간 복잡도 훨씬 개선됨 



