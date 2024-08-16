from copy import deepcopy

n = int(input())
triangle = [[0]*n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        triangle[i][j] = line[j]

# 입력 받은 삼각형과 동일한 dp 테아블 만들기
dp = deepcopy(triangle) 

# triangle과 dp 테이블이 각각 필요한 이유는, 비교 후 한 줄씩 계산할 때 임시 공간을 사용하도록 설계하였기 때문이다.
for i in range(n-1): 
    for j in range(i+1):
        x = triangle[i+1][j] + triangle[i][j]
        dp[i+1][j] = max(dp[i+1][j], x)
        y = triangle[i+1][j+1] + triangle[i][j]
        dp[i+1][j+1] = max(dp[i+1][j+1], y)
    # 
    triangle[i+1] = deepcopy(dp[i+1])

# 원래 이중 리스트 내 최대값 찾을 때 이중 반복문을 썼는데, map을 통해 더 간단하게 코드 구현
answer = max(map(max, dp))

print(answer)

"""
아래 코드는 다른 분이 작성한 코드. 공간 복잡도가 더 낮고, 코드 자체도 더 간결하다
내가 추가 공간을 사용한 것을 조건문을 여러 개 사용하여 구현한 것으로 이해하였다.

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:	# 왼쪽 끝이면
                triangle[i][j] += triangle[i-1][0]  # 이전 층의 0번째 값 더하기
            elif j == len(triangle[i])-1:	# 오른쪽 끝이면
                triangle[i][j] += triangle[i-1][-1]	# 이전 층의 -1번째 값 더하기
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

    return max(triangle[-1])
"""