array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

# x는 찾고자 하는 값, 결과는 찾고자 하는 값의 인덱스
def binary_search(array, x, start, end):
    mid = (start+end) // 2
    if start > end:
        return None
    elif array[mid] == x:
        return mid
    elif array[mid] > x:
        return binary_search(array, x, start, mid-1)
    elif array[mid] < x:
        return binary_search(array, x, mid+1, end)
    
print(binary_search(array, 512, 0, len(array)-1))