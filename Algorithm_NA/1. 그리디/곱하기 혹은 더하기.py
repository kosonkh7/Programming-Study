"""
입력값: 각 자리가 0~9로 이루어진 문자열 S
출력값: 해당 문자열 사이에 연산 기호를 삽입하여 만들 수 있는 최대값 

S의 길이는 20 이하, 가장 큰 수는 20억 미만이 되도록 주어짐
"""

s = input()
s_list = []

for i in s:
    s_list.append(int(i))

result = s_list[0]

# 0, 1일 때는 더하고, 나머지 수일 때는 곱하기
for i in range(1, len(s_list)):
    if result == 0 or s_list[i] == 0:
        result += s_list[i]
    elif result == 1 or s_list[i] == 1:
        result += s_list[i]
    else:
        result = result * s_list[i]

print(result)