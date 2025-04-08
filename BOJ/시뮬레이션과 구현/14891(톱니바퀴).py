n_list = [[int(i) for i in input()] for _ in range(4)]

n = int(input())

# 회전 방향에 따라 회전시키는 함수
def turn(n_list, d):
    if d == 1:
        tmp = [n_list[-1]] + n_list[0:7]
    elif d == -1:
        tmp = n_list[1:8] + [n_list[0]]
    else:
        tmp = n_list
    
    return tmp


# 1, 2, 3, 4 일때 각각 경우의 수 다 만들어버리기
def trial(x, d):
    if x == 1:
        d0 = d
        if n_list[0][2] == n_list[1][6]:
            d1 = 0
            d2 = 0
            d3 = 0
        elif n_list[1][2] == n_list[2][6]:
            d1 = d0 * (-1)
            d2 = 0
            d3 = 0
        elif n_list[2][2] == n_list[3][6]:
            d1 = d0 * (-1)
            d2 = d1 * (-1)
            d3 = 0
        else:
            d1 = d0 * (-1)
            d2 = d1 * (-1)
            d3 = d2 * (-1)
        n0, n1, n2, n3 = turn(n_list[0], d0), turn(n_list[1], d1), turn(n_list[2], d2), turn(n_list[3], d3)
        n_list[0], n_list[1], n_list[2], n_list[3] = n0, n1, n2, n3
    
    if x == 2:
        d1 = d
        if n_list[0][2] == n_list[1][6]:
            d0 = 0
        else:
            d0 = d1 * (-1)

        if n_list[1][2] == n_list[2][6]:
            d2 = 0
            d3 = 0
        elif n_list[2][2] == n_list[3][6]:
            d2 = d1 * (-1)
            d3 = 0
        else:
            d2 = d1 * (-1)
            d3 = d2 * (-1)
        n0, n1, n2, n3 = turn(n_list[0], d0), turn(n_list[1], d1), turn(n_list[2], d2), turn(n_list[3], d3)
        n_list[0], n_list[1], n_list[2], n_list[3] = n0, n1, n2, n3
    
    if x == 3:
        d2 = d
        if n_list[2][2] == n_list[3][6]:
            d3 = 0
        else:
            d3 = d2 * (-1)
        
        if n_list[1][2] == n_list[2][6]:
            d0 = 0
            d1 = 0
        elif n_list[0][2] == n_list[1][6]:
            d0 = 0
            d1 = d2 * (-1)
        else:
            d1 = d2 * (-1)
            d0 = d1 * (-1)
        n0, n1, n2, n3 = turn(n_list[0], d0), turn(n_list[1], d1), turn(n_list[2], d2), turn(n_list[3], d3)
        n_list[0], n_list[1], n_list[2], n_list[3] = n0, n1, n2, n3
            

    if x == 4:
        d3 = d
        if n_list[2][2] == n_list[3][6]:
            d0 = 0
            d1 = 0
            d2 = 0
        elif n_list[1][2] == n_list[2][6]:
            d0 = 0
            d1 = 0            
            d2 = d3 * (-1)
        elif n_list[0][2] == n_list[1][6]:
            d0 = 0
            d2 = d3 * (-1)
            d1 = d2 * (-1)
        else:
            d2 = d3 * (-1)   
            d1 = d2 * (-1)
            d0 = d1 * (-1)
        n0, n1, n2, n3 = turn(n_list[0], d0), turn(n_list[1], d1), turn(n_list[2], d2), turn(n_list[3], d3)
        n_list[0], n_list[1], n_list[2], n_list[3] = n0, n1, n2, n3
            
                     

for _ in range(n):
    x, d = map(int, input().split())
    trial(x, d)

print(n_list[0][0] + n_list[1][0] * 2 + n_list[2][0] * 4 + n_list[3][0] * 8)







