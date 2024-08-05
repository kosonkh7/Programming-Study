"""
n: 물건 개수
k: 배낭 최대 무게
w, v: (무게, 가치)

k 이하 무게 담았을 때 최대 가치 구하기.
"""

n, k = map(int, input().split())
dp = [0]*(k+1)
item = []

# 물건 무게가 최대 무게보다 무거우면 넘김
for i in range(n):
    w, v = map(int, input().split())
    if w > k:
        continue
    else:
        item.append([w, v])

# 배낭 문제는 정렬하지 않아도 된다.
# item.sort()

# 반복문 범위를 역방향으로 해야 중복 아이템 사용하지 않음을 보장한다고 한다.
for w, v in item:
    for j in range(k, w - 1, -1): # 이 부분 분명한 이해 필요
        dp[j] = max(dp[j], dp[j - w] + v)

print(max(dp))


"""
배낭 문제에서 역순으로 인덱스를 지정해야만, 아이템을 중복으로 사용하는 것을 방지할 수 있다. 명심할 것.
순방향 반복: 낮은 인덱스부터 높은 인덱스로 dp 배열을 업데이트하면, 이미 업데이트된 값이 다시 사용되어 동일한 아이템을 여러 번 사용하는 오류가 발생할 수 있습니다.
역순 반복: 높은 인덱스부터 낮은 인덱스로 dp 배열을 업데이트하면, 이미 업데이트된 값이 다시 사용되지 않으므로 각 아이템이 한 번만 사용되도록 보장할 수 있습니다.

for w, v in item:
    for j in range(0, k-w+1):
        dp[w+j] = max(dp[w+j], dp[j] + v)
"""