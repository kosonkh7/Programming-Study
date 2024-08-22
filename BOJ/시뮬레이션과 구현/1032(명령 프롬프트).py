n = int(input())

text = []

for i in range(n):
    x = input()
    text.append(x)

target = text[0]
answer = ''

for j in range(len(target)):
    x = target[j]
    for i in range(n):
        if text[i][j] != target[j]:
            x = '?'
            break
    answer += x

print(answer)