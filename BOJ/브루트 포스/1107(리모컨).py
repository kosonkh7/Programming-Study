"""
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 
채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
수빈이가 지금 보고 있는 채널은 100번이다.

첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다. 
둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 
고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.
출력: 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번
"""

n = int(input())
m = int(input())

# 1. 고장난 버튼 리스트 - 고장난 버튼 없으면 입력 안 받기
if m != 0:
    m_list = list(input().split())
else:
    m_list = []

# 2. 고장 안 난 버튼 리스트 m_list_r
lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
m_list_r = [i for i in lst if i not in m_list]


def find_near(n, m_list_r):
    dif = abs(n-100) # 초기값: 100에서 + -만 누르기
    x = 100
    con = True
    for i in range(0, 1000200): # 범위를 이렇게 많이 하는 게 걸렸지만, 시간 복잡도 넘지 않을 것으로 예상 하였다.
        con = True
        # i를 리모컨으로 만들 수 있으면 True, 없으면 False
        for j in str(i):
            if j not in m_list_r:
                con = False
                break
        # 만들 수 있으면 
        if con == True:
            if dif < abs(n-i) + len(str(i)):
                pass
            else:
                x = i
                dif = abs(n-i) + len(str(i))
    
    return dif

answer = find_near(n, m_list_r)
if answer < abs(n-100):
    print(answer)
else: print(abs(n-100))