# 답은 맞는데 시간 초과 발생
# 대각선으로 이동할 때, 행과 열의 규칙이 존재한다는 점을 바탕으로 개선 가능
# 백트래킹 대표 예제이므로 다시 풀어보기

n = int(input())
answer = 0

def dfs(n_list):
    global answer
    if len(n_list) == n:
        # print(n_list)
        answer += 1
        return
    elif n_list == []:
        for i in range(n):
            n_list.append(i)
            dfs(n_list)
            n_list.pop()
    else:
        for i in range(n):
            ban_list = []
            for j in range(len(n_list)): # 대각선 고려하는 과정에서 시간 초과 발생. 위 설명을 바탕으로 수정해보자
                ban_list.append(n_list[j] + (len(n_list) - j))
                ban_list.append(n_list[j] - (len(n_list) - j))

            if i not in n_list and i != n_list[-1] + 1 and i != n_list[-1] - 1 and i not in ban_list:
                n_list.append(i)
                dfs(n_list)
                n_list.pop()

dfs([])

print(answer)