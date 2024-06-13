"""
입력값: 떡의 개수 N, 손님이 요청한 길이 M / 둘째 줄엔 떡의 개별 높이
출력값: 적어도 M만큼 떡을 가져가기 위한 절단기 길이의 최대값
"""

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)

# 내가 처음으로 구현한 코드. 재귀적으로 구현하였고, 정상적으로 작동하지만,
x = array[0]-1
# 최악의 경우 시간 복잡도가 O(n^2)이다.
def optimize(array, x):
    result = 0
    for i in range(len(array)):
        if array[i] > x:
            result += (array[i]-x)
        else:
            break
    if result >= m:
        return x
    else:
        return optimize(array, x-1)        

a = optimize(array, x)

# print(a)

"""
대충 범위가 10억 이상인 경우에 일단 이진탐색을 떠올리면 좋다고 한다.

문제 분석은 잘한 것 같은데 이진탐색 구현이 아직 어색했다.

아래는 이진탐색 + 반복문으로 구현한 모범답안
"""

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)