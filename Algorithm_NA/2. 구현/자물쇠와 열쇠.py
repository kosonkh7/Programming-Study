"""
입력값: 키 MxM 배열, Lock NxN 배열, M은 언제나 N보다 작으며 20이하이다.
출력값: 회전 또는 이동하여 락이 전부 채워지면 True, 그렇지 않으면 False

입력값 범위가 작으니 그리디, 완탐을 고려해본다.
네 방향 전부 돌리고, 모든 이동을 고려해보기

- 놓친 점: 이동을 어떤 방식으로 구현할지 고민해봤는데, Lock의 크기를 키워서 더한 뒤 가운데 부분만 맞는지 조사해보는 방향이 좋다고 한다.

회전 함수 -> 락 확장 -> 체크 함수 순으로 만들기.
"""

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


# 회전 함수
def rotate(key, i):
    n = len(key[0])-1
    if i == 0:
        return key
    elif i == 1:
        rotate_key = key.copy()
        for i in range(n):
            for j in range(n):
                rotate_key[j][n-i] = key[i][j]
        return rotate_key
    elif i == 2:
        rotate_key = key.copy()
        for i in range(n):
            for j in range(n):
                rotate_key[n-i][n-j] = key[i][j]
        return rotate_key
    elif i == 3:
        rotate_key = key.copy()
        for i in range(n):
            for j in range(n):
                rotate_key[n-j][i] = key[i][j]
        return rotate_key


# 체크 함수 필요
# n = len(lock[0])
# m = len(key[0])

# expanded_lock = [[0] * (n+2*m-1) for _ in range(n+2*m-1)]

# for i in range(m-1, n+m-1):
#     for j in range(m-1, n+m-1):









def solution(key, lock):
    answer = True
    real_key = [[0]*len(lock) for _ in range(len(lock))]

    for i in range(len(lock)+len(key)-1):
        for j in range(len(lock)+len(key)-1):
            real_key[i][j] = 















    return answer