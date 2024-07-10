"""
입력값: 문자열 s (소문자로만 이루어짐, 길이 1000이하)
출력값: 문자를 규칙에 따라 압축했을 때, 압축된 길이가 가장 작은 것의 길이를 출력

최장패턴: 문자열 길이를 2로 나눈 몫

- 1부터 최장패턴까지 완전 탐색하려는 접근까진 적절했으나 이후 길이 
- 예시 답안들을 읽어보며 알게된 점은, 우선 문제에서 주어지는 규칙을 명확하게 숙지하지 못한 탓이 있고, (지문을 꼼꼼하게 정독할 것!)
- 반복문에 step 지정하는 등, 문법을 알고 있으나 자주 활용하지 않은 것을 적절하게 떠올리지 못하였다.
- 다시 풀어볼 것
"""

s = 'abcdefgabcdefgabcdefgabcdefgabcdefgeeeeabcdefgabcdefg'

# 예시 답안
def solution(s):
    answer = len(s)
    # 원래 문자열 길이가 2이하면 그대로 반환
    if answer <= 2: return answer
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2 + 1):
        compressed = ''
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위 크기(step)만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count+=1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    
    return answer

print(solution(s))