"""
식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
음수를 양수로 나눌 때는 C++14의 기준을 따른다. 
즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.

1. 연산기호로 이뤄진 리스트 만들기 : cal_list
2. 연산기호 순서 모든 경우의 수 조합 만들기 : cal_list (헷갈려서 그냥 같은 변수에 뒤집어씌움, set 이용해서 중복 제거)
3. eval 기준 별도의 연산식 만들어줌 : custom_eval (음수를 양수로 나눌 때 C++14의 기준 나눗셈 적용하기 위함 -> 그냥 해봤더니 문제 의도와 연산 결과가 다름)
4. 모든 경우의 수 계산
"""
import math
from itertools import permutations
max_answer = -9999999999999
min_answer = 99999999999999

n = int(input())
n_list = list(map(int, input().split()))
tmp = list(map(int, input().split()))

# 1. 연산기호로 이뤄진 리스트 만들기 : cal_list
cal_list = []
for i in range(4):
    if i == 0:
        for j in range(tmp[i]):
            cal_list.append('+')
    if i == 1:
        for j in range(tmp[i]):
            cal_list.append('-')            
    if i == 2:
        for j in range(tmp[i]):
            cal_list.append('*')
    if i == 3:
        for j in range(tmp[i]):
            cal_list.append('/')                

# 2. 연산기호 순서 모든 경우의 수 조합 만들기 : cal_list (헷갈려서 그냥 같은 변수에 뒤집어씌움, set 이용해서 중복 제거)
cal_list = set(permutations(cal_list))

# 3. eval 기준 별도의 연산식 만들어줌 : custom_eval (음수를 양수로 나눌 때 C++14의 기준 나눗셈 적용하기 위함 -> 그냥 해봤더니 문제 의도와 연산 결과가 다름)
def custom_eval(answer_str):
    # 나눗셈을 먼저 계산
    result = eval(answer_str)
    
    # 0쪽으로 버림을 적용
    if result < 0:
        return math.ceil(result)
    return math.floor(result)

# 4. 모든 경우의 수 계산
for cal in cal_list:
    cal = list(cal)
    answer_str = str(n_list[0])
    for i in range(n-1):
        answer_str = answer_str + cal[i]
        answer_str = answer_str + str(n_list[i+1])

        answer_str = str(custom_eval(answer_str))
    
    if int(answer_str) > max_answer:
        max_answer = int(answer_str)
    
    if int(answer_str) < min_answer:
        min_answer = int(answer_str)

print(max_answer)
print(min_answer)