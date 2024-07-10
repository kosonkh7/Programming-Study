"""
https://youtu.be/zpz8SMzwiHM
다시 풀어보기. 어렵다.
아래 풀이로 풀면 시간 복잡도 해결 못함.
"""

food_times = [3, 1, 2, 5, 6]
k = 10


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    answer = 0
    # 음식의 가짓수 n
    n = len(food_times)
    # 비었으면 False로 변환
    q = [True]*n

    while k>0:
        if q[answer] == False:
            answer += 1
            continue
        else:
            food_times[answer] -= 1
            if food_times[answer] == 0:
                q[answer] = False
            answer += 1
            if answer == n:
                answer = 0
            k -= 1
    return answer+1 

a = solution(food_times, k)

print(a)

"""
나동빈님 예시 답안.
내 문제-> 일단 시간 효율적으로 계산하는 수학적인 접근 방식에 도달하지 못 했던 게 첫 번째 문제
그리고 시간 효율적으로 구현하기 위해 우선순위 큐나 리스트 정렬을 '적절하게 떠올려서 적용시키지 못했'기에 헤맸다.
예시 코드 자체는 이해 완료.
"""
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면
    if sum(food_times) <= k:
        return -1
    
    # 시간이 작은 음식부터 빼야하므로 우선순위큐를 사용한다.
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위큐에 삽입 (i+1인 이유는 인덱스 맞춰주기 위함)
        heapq.heappush(q, (food_times[i], i+1))
    
    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 음식 시간
    previous = 0
    # 남은 음식의 개수
    length = len(food_times)


    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:    
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정
    
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1]) # 음식의 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]



"""
카카오 코테는 기본 코드가 주어지나보다.


각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 
네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 
몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.

# 정확성 테스트 제한 사항
food_times 의 길이는 1 이상 2,000 이하이다.
food_times 의 원소는 1 이상 1,000 이하의 자연수이다.
k는 1 이상 2,000,000 이하의 자연수이다.

# 효율성 테스트 제한 사항 (시간 복잡도 고려해라는 뜻)
food_times 의 길이는 1 이상 200,000 이하이다.
food_times 의 원소는 1 이상 100,000,000 이하의 자연수이다.
k는 1 이상 2 x 10^13 이하의 자연수이다.

입력값: food_times(ex. [3, 1, 2]), 지연 시간 k
출력값: k초 후 몇 번 음식을 먹어야 하는지. (먹을 게 없으면 -1)
"""

