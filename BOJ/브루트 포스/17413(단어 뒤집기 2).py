s = input()
tmp = ''
answer = ''

is_list = False
for i in range(len(s)):
    if s[i] == '<':
        answer = answer + tmp[::-1]
        is_list = True
        tmp = '<'
    elif s[i] == '>':
        answer = answer + tmp + '>'
        is_list = False
        tmp = ''
    elif s[i] == ' ' and not is_list:
        answer = answer + tmp[::-1] + ' '
        tmp = ''
    else:
        tmp = tmp + s[i]


answer = answer + tmp[::-1]
print(answer)