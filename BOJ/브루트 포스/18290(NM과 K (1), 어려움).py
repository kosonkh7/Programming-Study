"""
백트래킹에 대한 이해 필요.

if ok: 다음 코드가 중요
"""

n, m, k = map(int, input().split())  # n: 행의 수, m: 열의 수, k: 선택할 칸의 수
arr = [list(map(int, input().split())) for _ in range(n)]  # n x m 크기의 2차원 배열 입력
visited = [[False] * m for _ in range(n)]  # 방문 여부를 체크하기 위한 2차원 배열

# 동서남북 방향을 나타내는 델타 배열
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -1000000  # 정답을 저장할 변수, 초기값은 충분히 작은 값으로 설정

def go(px, py, index, sum):
    # k개의 칸을 모두 선택했을 때
    if index == k:
        global answer
        if answer < sum:  # 현재까지의 합이 기존의 answer보다 크면 갱신
            answer = sum
        return
    
    # 현재 위치에서부터 n행까지 반복
    for x in range(px, n):
        # 현재 행이 px라면 py부터, 그렇지 않다면 0부터 m열까지 반복
        for y in range(py if x == px else 0, m):
            if visited[x][y]:  # 현재 위치를 이미 방문했는지 확인
                continue
            ok = True
            # 동서남북 네 방향을 확인하여 인접한 칸이 방문되었는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:  # 인접한 칸이 배열의 범위를 벗어나지 않는지 확인
                    if visited[nx][ny]:  # 인접한 칸이 이미 방문되었으면
                        ok = False  # 현재 칸을 선택할 수 없음

            # 현재 칸을 선택할 수 있는 경우
            if ok:
                visited[x][y] = True  # 현재 칸을 방문한 것으로 표시
                go(x, y, index + 1, sum + arr[x][y])  # 다음 단계로 재귀 호출
                visited[x][y] = False  # 현재 칸을 다시 미방문 상태로 복구

# 초기 호출: (0, 0)에서 시작, 선택한 칸의 수 0, 합계 0
go(0, 0, 0, 0)

# 최종 결과 출력
print(answer)