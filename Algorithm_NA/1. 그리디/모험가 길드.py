"""
입력값: 모험가 수 N, 각 모험가의 공포도 (N 이하)
출력값: 여행을 떠날 수 있는 그룹 수의 최대값

공포도가 X인 모험가는 꼭 X명 이상으로 구성된 그룹에 포함되어야만 한다.
"""

# 모험가 수
n =  int(input()) 
# 모험가 공포도 입력 받아 오름차순으로 정렬
n_list = list(map(int, input().split()))
n_list.sort()

# 그룹 수
count = 0

while len(n_list) >= 1:
    # 그룹 배정 안 받은 모험가 중, 가장 큰 공포도보다 남은 인원의 수가 같거나 클 때 새 그룹 생성
    if n_list[-1] > len(n_list):
        break
    # 가장 공포도 큰 모험가의 공포도 x
    x = n_list.pop()
    # 가장 큰 공포도만큼 전체 인원에서 빼줌
    for i in range(x-1):
        n_list.pop()
    # 그룹 생성 완료했다는 의미
    count += 1
    #print(n_list) <- 과정을 보고 싶을 때 출력해보기

print(count)


"""
모범 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
"""
