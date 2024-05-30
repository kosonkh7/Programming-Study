"""
입력값: N
00시 00분 00초 ~ N시 59분 59초 사이에 3이 하나라도 등장하는 경우의 수를 출력한다.
"""
# 경우의 수 60*60

n = int(input())

count = 0

for i in range(0, n+1):
    if i in (3, 13, 23):
        count += (60*60)
    else:
        count += (10*60 + 5*60 + 45*10 + 45*5)

print(count)



"""
모범답안:

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if 3 in str(i)+str(j)+str(k):
                count+=1

"""