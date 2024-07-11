"""
에라토스테네스의 체에 대해 자세히 알아볼 것
"""


max = 1000000

dp = [0] * (max+1)
dp[0] = -1

lst = []

# 1. 소수 판별 테이블 만들기
for i in range(2, max+1):
    j = i
    if dp[i] == 0:
        lst.append(i)
        dp[i] = i
        while i*j <= max:
            dp[i*j] = -1
            j += 1
    else: continue

# 2. 소수만 존재하는 테이블로 변환
# lst = [dp[i] for i in range(len(dp)) if dp[i] == i]

# 3. 모든 조합을 구하여 소수의 합 테이블을 만든다. 근데 이게 시간 복잡도가 최대 2^n..?
# from itertools import combinations
# # sum_list = [x + y for x, y in combinations(lst, 2)]
# value_list = combinations(lst, 2)
# sum_list = [x + y for x, y in value_list]

# while True:
#     n = int(input())
#     if n == 0: break
#     else:
#         if n in sum_list:
#             print(f'{n} = {value_list[sum_list.index[n][0]]} + {value_list[sum_list.index[n][1]]}')
#         else:
#             print("Goldbach's conjecture is wrong.")     

# 시간 초과
while True:
    con = False
    n = int(input())
    if n == 0: break
    else:
        for i in lst:
            if n-i in lst:
                print(f'{n} = {i} + {n-i}')
                con = True
                break
    if con == False:
        print("Goldbach's conjecture is wrong.")            
        


