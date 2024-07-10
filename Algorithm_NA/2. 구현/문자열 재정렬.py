"""
입력값: 알파뱃과 숫자로 혼합된 문자열
출력값: 알파뱃과 숫자 순서로 정렬하여 출력 (예: ABC123)
"""
# 입력 받아서 리스트로 저장, 정렬 (숫자-알파뱃 순으로 정렬)
s = input()
s_list = [i for i in s]
s_list.sort()

# 숫자와 알파뱃 구분 인덱스 찾는 반복문
x = 0

for i in range(len(s_list)):
    if s_list[i].isdigit() == False:
        x = i
        break

# 숫자와 알파뱃 구분
s_num = s_list[0:x]
s_alphabet = s_list[x:]

# 알파뱃 뒤에 숫자 붙여 넣고
for i in s_num:
    s_alphabet.append(i)

# 출력
for i in s_alphabet:
    print(i, end='')