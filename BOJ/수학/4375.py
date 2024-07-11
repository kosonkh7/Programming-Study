# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
# 테스트 케이스로 이루어져있다 -> try-except 구문으로 접근

while True:
    try:
        n = int(input())
    except:
        break
    
    x = 1
    tmp = 1

    while True:
        if x % n == 0:
            break
        else:
            tmp *= 10
            x += tmp

    # print(x)
    print(len(str(x)))