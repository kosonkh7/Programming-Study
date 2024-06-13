"""
입력값: 재고가 있는 N개(첫째 줄)의 부품 번호(둘째 줄), 손님이 원하는 M개(셋째 줄)의 부품 번호(넷째 줄)
출력값: 손님이 원하는 부품이 있는지 각각 yes, no로 출력
"""

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort() # 처음부터 set() 자료형에 저장하면 따로 정렬할 필요도 없다.

def Is_stock(n_list, x, start, end):
    if start > end:
        return 'no'
    mid = (start+end) // 2
    if n_list[mid] == x:
        return 'yes'
    elif n_list[mid] < x:
        return Is_stock(n_list, x, mid+1, end)
    elif n_list[mid] > x:
        return Is_stock(n_list, x, start, mid-1)

result = []

for i in m_list:
    result.append(Is_stock(n_list, i, 0, len(n_list)-1))

for i in result:
    print(i, end=' ')

"""
위 문제는 계수정렬로 접근 가능하다.
부품번호는 범위가 있으므로 (1~100,000), 부품이 있으면 1, 없으면 0인 길이가 100,000인 인덱스 리스트를 만들어   
해당 부품이 있는지 없는지 확인하는 코드로 작성할 수 있다.
꼭 이진탐색이 아니더라도 다양한 자료형을 바탕으로 구현할 수 있다.
"""