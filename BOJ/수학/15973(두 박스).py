# 15973 두 박스
"""
x = list(map(int, input().split()))
y = list(map(int, input().split()))

if x[2] < y[0] or x[3] < y[1] or y[2] < x[0] or y[3] < x[1]:
    print('NULL')
elif x[2] == y[0] or y[2] == x[0]:
    if x[1] == y[3] or y[1] == x[3]:
        print('POINT')
    else:
        print('LINE')
elif x[1] == y[3] or y[1] == x[3]:
    print('LINE')
else:
    print('FACE')
"""