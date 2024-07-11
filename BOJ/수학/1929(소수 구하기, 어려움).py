# m, n = map(int, input().split())

# # 소수 저장하는 테이블
# table = [2]

# # 소수이면 True, 아니면 False
# con = True

# # 소수인 테이블 내 값들로 나눠보고, 나눠 떨어지는 게 없으면 소수 테이블에 그 값 추가
# for i in range(3, n+1):
#     for j in table:
#         if i % j == 0:
#             con = False
#             break
#     if con == False:
#         con = True
#     elif con == True:
#         table.append(i)

# for i in table:
#     if i >= m and i<=n:
#         print(i)

"""
17425 약수의 합 참고
while문 -> 조화급수 형태 가지면 nlogn 시간복잡도 갖는 것 이용
"""


max = 1000000

dp = [0] *(max+1)


for i in range(2, max+1):
    if dp[i] == 0:
        dp[i] = i
        j = 2
        while i*j <= max:
            dp[i*j] = -1
            j+=1
    else: continue

m, n = map(int, input().split())

for i in dp[m:n+1]:
    if i >= 2:
        print(i)

