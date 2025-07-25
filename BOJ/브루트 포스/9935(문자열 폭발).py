# 스택으로 풀면 풀린다고 한다.
# 아래와 같이 풀면 아마 내장함수(len)가 시간복잡도가 커서 초과되는 듯하다.
x = input()
y = input()

while x != '':
    tmp = len(x)
    x = x.replace(y, '')
    if tmp == len(x):
        break

if x == '':
    print('FRULA')
else: print(x)