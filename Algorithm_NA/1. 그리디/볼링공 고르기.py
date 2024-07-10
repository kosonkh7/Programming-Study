"""
입력값: 볼링공 개수 N, 볼링공 최대 무게 M | 각 볼링공 무게
출력값: 서로 무게가 다른 볼링공을 고르는 방법 가짓 수
"""

n, m = map(int, input().split())

n_list = list(map(int, input().split()))

count = 0

for i in range(n-1):
    for j in range(i, n):
        if n_list[i] != n_list[j]:
            count += 1

print(count)

"""
내가 작성한 코드는 연산량이 n^2 (최대 1000*1000)

모범답안은 M이 최대 10인 걸 이용하여 시간복잡도가 O(N)이므로  훨씬 낮다
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱해주기

print(result)
"""