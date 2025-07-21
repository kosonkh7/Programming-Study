"""
그냥 알고리즘 짜는 건 쉽게 했는데
문자열 처리를 위한 함수, 자료형(deque) 처리 함수를 알아야만 쉽게 풀 수 있었다
시험 전에 익혀갈 것

4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""
from collections import deque

# 출력 조건에 맞게 리스트의 공백 없이 출력하기 위한 함수
def print_list_no_space(lst):
    print("[" + ",".join(map(str, lst)) + "]")

t = int(input())
for i in range(t):
    orders = input() # 명령
    n = int(input())
    tmp = input() # 입력값을 리스트로 바꾸기 위한 임시 변수
    tmp = tmp[1:-1]
    if tmp == '': # 처음부터 공백 리스트 주어졌을 때의 예외 처리
        n_list = deque([])
    else:
        n_list = deque(list(map(int, tmp.split(','))))
    reverse = 1 # -1이면 뒤집힌 거. 

    error = False # 리스트 비어 있는데 D 명령 수행하면 에러 처리.
    for order in orders:
        if order == 'R':
            reverse *= (-1)
        elif n_list == deque([]):
            error = True
            break
        else:
            if reverse == 1: # 뒤집혔는지 여부에 따라 처음을 뺄지, 끝을 뺄지
                _ = n_list.popleft()
            else:
                _ = n_list.pop()

    answer = list(n_list)

    if error == True:
        print('error')
    elif reverse == 1:
        print_list_no_space(answer)
    else:
        answer.reverse()
        print_list_no_space(answer)