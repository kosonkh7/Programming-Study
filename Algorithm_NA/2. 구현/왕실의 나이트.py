"""
8x8 체스판 위에 나이트가 움직일 수 있는 경우의 수를 구한다.
입력값: 체스판 위 나이트의 좌표 (ex. a1, b5, d6)
출력값: 나이트가 판 위에서 움직일 수 있는 경우의 수

경우의 수의 최대값은 8이 된다
"""

location = input()

x_str = location[0]
y = int(location[1])

alp_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
int_list = [1, 2, 3, 4, 5, 6, 7, 8]

x = 0

def change_int(x):
    a=0
    for i in range(len(alp_list)):
        if x == alp_list[i]:
            a = int_list[i]
    return a

x = change_int(x_str)

count = 0

available = [[x+1, y+2],[x+1, y-2],[x-1, y+2],[x-1, y-2],[x+2, y-1],[x+2, y+1],[x-2, y+1],[x-2, y-1]]

for i, j in available:
    if i >= 1 and i <=8 and j >= 1 and j <=8:
        count+=1

print(count)
