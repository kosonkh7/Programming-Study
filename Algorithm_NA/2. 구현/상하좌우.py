n = int(input())
plans = list(input().split()) #L R U D

x = 0
y = 0

for i in plans:
    if i == 'L':
        if x <= 0:
            continue
        else:
            x -= 1
    elif i == 'R':
        if x >= (n-1):
            continue
        else:
            x += 1
    elif i == 'U':
        if y <= 0:
            continue
        else:
            y -= 1    
    elif i == 'D':
        if y >= (n-1):
            continue
        else:
            y += 1

print(x+1, y+1, sep=' ')   