"""
입력값: 0과 1로 이루어진 문자열 S
출력값: 뒤집었을 때 전부 같은 수가 되도록 만드는 최소값

기준 값과 비교했을 때 이어지는 수가 다르면 +1하고 기준값 변경, 같으면 넘김
"""

s = input()

# 너무 단순하게 생각해서 시간 복잡도 너무 큰 방법
# def change(_):
#     for i in range(len(_)):
#         if _[i] == '1':
#             _[i] = '0'
#         else: _[i] = '1'

now = s[0]
count0 = 0
count1 = 0

# 첫 번째 원소에 대해서 처리 <- 이 부분 작성하지 못해서 헤맴
if now == '1':
    count0 += 1
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i] != now and s[i] == '0':  
        count1 += 1
        now = s[i]
    elif s[i] != now and s[i] == '1':
        count0 += 1
        now = s[i]

print(min(count0, count1))

