"""
피보나치 수열 100번째 값을 구하라

1, 1, 2, 3, 5, 8, 13, 21 ....
"""

# DP 테이블 초기화
dp_table = [0] * 100

dp_table[0], dp_table[1] = 1, 1

# 다이나믹 프로그래밍으로 구현 (보텀업)
for i in range(2, 100):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]

print(dp_table[99])