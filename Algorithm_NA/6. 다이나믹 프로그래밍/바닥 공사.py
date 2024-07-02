"""
입력값: 타일 크기 N 
출력값: 2xN 크기의 타일을 채우는 모든 경우의 수를 796796으로 나눈 나머지를 출력하라

타일은 1X2, 2X1, 2X2 크기가 존재한다.

탑다운 방식으로 문제 해결하는 방안을 고민해보면서 보텀업으로 풀 수 있다.
""" 

n = int(input())

dp_table = [0] * 1001

dp_table[1] = 1
dp_table[2] = 3

for i in range(3, n+1):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]*2

print(dp_table[n] % 796796)
