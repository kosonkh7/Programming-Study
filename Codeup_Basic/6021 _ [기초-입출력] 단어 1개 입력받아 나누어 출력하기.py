"""

알파벳과 숫자로 이루어진 단어 1개가 입력된다.
입력받은 단어의 각 문자를 한 줄에 한 문자씩 분리해 출력한다.

예시
s = input()
print(s[0])
print(s[1])
...

참고
s[0] 은 첫 번째 문자를 의미한다.

"""


x = input()

for i in range(len(x)):
    print(x[i])
