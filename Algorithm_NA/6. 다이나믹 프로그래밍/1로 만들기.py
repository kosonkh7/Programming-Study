"""
입력값: 1~30000 사이의 정수
연산 4가지
- X가 5로 나누어 떨어지면 5로 나누기. 
- 3으로 나누기. 
- 2로 나누기.
- 1 빼기
4가지 연산을 사용하여 1로 만드는 최소값을 구하라


최악의 경우의 수: 1씩 계속 빼는 것
"""

x = int(input())

dp_table = [0] * 30001

# dp_table[2] = 1
# dp_table[3] = 1
# dp_table[4] = 2 # dp_table[3] + 1 or dp_table[2] + 1
# dp_table[5] = 1
# dp_table[6] = 2 # dp_table[5] + 1 or dp_table[2] + dp_table[3]
# dp_table[7] = 3 # dp_table[6] + 1 


for i in range(2, x + 1):
    dp_table[i] = 1 + dp_table[i-1]
    if i % 2 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//2] + 1)
    if i % 3 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//3] + 1)
    if i % 5 == 0:
        dp_table[i] = min(dp_table[i], dp_table[i//5] + 1)

print(dp_table[x])


