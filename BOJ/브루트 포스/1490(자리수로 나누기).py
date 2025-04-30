import math

n = input()
n_list = [int(i) for i in n]
n_lcm = 1
for i in n_list:
    n_lcm = math.lcm(n_lcm, i)


answer = n_lcm

# 83 -> 8304 같은 걸 반영 못하는 코드
if int(n) // n_lcm == 0:
    answer = n_lcm
else:
    tmp = 0
    length = 1 # n 뒤에 붙일 문자열 길이
    # 아직 수정 안했는데, 반복문을 통해 lentgh가 1이면 0~9까지
    # n = 2이면 length가 00~99까지 더해주면서 나머지가 0인지 확인하는 절차 가짐.
    while True:
        print(int(n + str(tmp)))
        if int(n + str(tmp)) % n_lcm == 0:
            answer = int(n + str(tmp))
            break
        else:
            tmp += 1


print(answer)