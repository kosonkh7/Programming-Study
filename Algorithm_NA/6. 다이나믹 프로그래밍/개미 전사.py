"""
입력값: 창고 개수 N개, 창고 내 각 식량 개수 K개 
출력값: 한 칸 이상 떨어진 창고를 털어서 최대 약탈 가능한 식량 개수


"""

k = int(input())
warehouse = list(map(int, input().split()))
dp_table = [0] * k

dp_table[0] = warehouse[0]
dp_table[1] = max(warehouse[0], warehouse[1])


for i in range(2, k):
    dp_table[i] = max(warehouse[i] + dp_table[i-2], warehouse[i-1])

print(dp_table[k-1])