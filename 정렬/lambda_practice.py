# 람다 언제 쓰냐 
# 1. 정렬 기준 키 줄 때 많이 씀 -> 왜?


def by_second(x):
    return x[1]

arr1 = [(1, 1), (3, 2), (3, 1)]
arr1.sort(key=by_second)

print(arr1)

arr2 = [(1, 1), (3, 2), (3, 1)]
arr2.sort(key=lambda x: x[1]) # 위의 함수랑 같은 뜻임
print(arr2)


# 2. map 함수에서의 사용 
nums = [1, 2, 3, 4]
print(list(map(lambda x: x*x, nums)))
