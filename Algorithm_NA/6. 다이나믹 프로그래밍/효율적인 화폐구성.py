"""
입력값: 화폐 종류 N, 목표값 M, N개의 화폐
출력값: 화폐로 M을 만들 수 있는 최소 화폐 개수
"""

n = int(input())
m = int(input())
n_list = list(map(int, input().split()))

dp_table = [10001] * (m+1)

for i in range(1, m+1):
    # 해당 화폐가 있는 건 무조건 1
    if i in n_list:
        dp_table[i] =  1
    # 목표 금액에 각 화폐를 한 번씩 뺀 값을 비교
    else:
        for k in n_list:
            dp_table[i] = min(dp_table[i], dp_table[i-k]+1)


if dp_table[m]>= 10001:
    print(-1)
else:
    print(dp_table[m])


"""
모범답안
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
"""