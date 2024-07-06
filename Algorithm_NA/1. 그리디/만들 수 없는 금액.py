"""
입력값: 동전 갯수 n | n개의 각 동전 금액
출력값: N개의 동전으로 만들 수 없는 금액의 최솟값
"""

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

# 이렇게 하면 시간 복잡도 초과함
# table = [False] * 1001
# table[0] = True
# table[n_list[0]] = True

# answer = -1

# def table_index(table):
#     _ = []
#     for i in range(len(table)):
#         if table[i] == True:
#             _.append(i)
#     return _

# for i in range(1, n):
#     table[n_list[i]] = True
#     for j in table_index(table):
#         table[n_list[i]+j] = True

"""
이 알고리즘의 핵심은 "현재 만들 수 있는 최대 금액 + 1"이 다음 동전의 액면가보다 작다면, 그 금액을 만들 수 없다는 것.

이걸 이해하지 못하면 내가 처음 짠 코드처럼 시간복잡도를 초과하게 된다.

모범답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
"""