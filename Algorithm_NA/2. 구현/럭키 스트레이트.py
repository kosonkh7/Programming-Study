"""
입력값: N
출력값: LUCKY 또는 READY

입력값의 중앙 자릿 수 기준으로 왼쪽과 오른쪽 합이 같을 때 럭키 스트레이트. 아니면 준비 상태
"""
# 입력값 문자열로 받기 
n = input()

# 자릿 수 중간 찾기 (나누기 할 때 정수로 바꾸는 거 필수!)
mid = int(len(n)/2)

# 중앙 기준으로 왼쪽 자릿수와 오른쪽 자릿수 하나씩 정수 형태로 리스트에 저장
left_list = [int(i) for i in n[0:mid]] 
right_list = [int(i) for i in n[mid:]] 

# 왼쪽 오른쪽 합 비교
if sum(right_list) == sum(left_list):
    print('LUCKY')
else: print('READY')
