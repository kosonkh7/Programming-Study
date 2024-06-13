# 선택 정렬
a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

print(a)

# 삽입 정렬 (수학적인 사고를 요하는 방식이기에 어려웠다)
b = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(b)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if b[j] < b[j - 1]: # 한 칸씩 왼쪽으로 이동
            b[j], b[j - 1] = b[j - 1], b[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(b)    

# 퀵 정렬
c = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 하나인 경우를 의미
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때따지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[right], array[left] = array[left], array[right]
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(c, 0, len(c) - 1)
print(c)

# 더 가독성 있는 방식으로 
# 이게 훨씬 이해하기 쉬움!
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort2(array))

