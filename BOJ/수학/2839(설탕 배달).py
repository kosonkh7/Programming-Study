n = int(input())

answer = 0
i = 1

if n % 5 == 0:
    answer = n // 5
elif n == 3 or n == 6 or n == 9 or n == 12:
    answer = n // 3
else:
    while i < 5 and n > 5:
        n -= 3
        if n % 5 == 0:
            answer = i + n // 5
            break
        i += 1


print(answer)