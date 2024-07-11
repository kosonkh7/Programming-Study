"""
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.
가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.
사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)
다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.
사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

최대로 먹을 수 있는 개수는 N일 것이다.

일단 바꾸는 것 없이 조사하는 방법부터 알아보자.
"""

n = int(input())

n_list = [list(input()) for _ in range(n)]


# 1. 연속적인 사탕 개수 찾기
def count_candy(n_list):
    max_num = 1
    # 가로 확인
    for i in range(n):
        sum = 1
        for j in range(n-1):
            if n_list[i][j] == n_list[i][j+1]:
                sum += 1
            else:
                sum = 1
            max_num = max(sum, max_num)

    # 세로 확인
    for i in range(n):
        sum = 1
        for j in range(n-1):
            if n_list[j][i] == n_list[j+1][i]:
                sum += 1
            else:
                sum = 1
            max_num = max(sum, max_num)

    return max_num

# 2. swap할 수 있는 모든 경우의 수를 대상으로 연속적인 사탕 수 계산
answer = count_candy(n_list)

# 가로로 swap
for i in range(n):
    for j in range(n-1):
        swap_list = n_list # 이 부분 copy.deepcopy로 했으면 아래 문장 추가 없이 됐을 수도
        swap_list[i][j], swap_list[i][j+1] = swap_list[i][j+1], swap_list[i][j]
        answer = max(answer, count_candy(swap_list))
        swap_list[i][j], swap_list[i][j+1] = swap_list[i][j+1], swap_list[i][j] # 추가한 문장

# 세로로 swap
for i in range(n):
    for j in range(n-1):
        swap_list = n_list # 이 부분 copy.deepcopy로 했으면 아래 문장 추가 없이 됐을 수도
        swap_list[j][i], swap_list[j+1][i] = swap_list[j+1][i], swap_list[j][i]
        answer = max(answer, count_candy(swap_list))
        swap_list[j][i], swap_list[j+1][i] = swap_list[j+1][i], swap_list[j][i] # 추가한 문장

print(answer)

