n, k = map(int, input().split())

belt = list(map(int, input().split()))
robot = [0] * (2*n)
answer = 0

while True:
    answer += 1

    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전.
    belt = [belt[-1]] + belt[:2*n-1]
    robot = [robot[-1]] + robot[:2*n-1]
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다
    for i in range(2*n-1, -1, -1):
        if robot[i] == 1:
            # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
            if i+1 != 2*n:
                if belt[i+1] > 0 and robot[i+1] == 0:
                    belt[i+1] -= 1
                    robot[i+1] = 1
                    robot[i] = 0
            # 2n칸에서 1로 넘어가는 경우 예외 처리
            else:
                if belt[0] > 0 and robot[0] == 0:
                    belt[0] -= 1
                    robot[0] = 1
                    robot[i] = 0
        # 로봇이 내리는 칸에 도달하면 언제든 내린다.
        if robot[n-1] == 1:
            robot[n-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    tmp = 0
    for i in belt:
        if i == 0:
            tmp += 1
    
    # print(f"{answer}st trial")
    # print(belt)
    # print(robot)

    if tmp >= k:
        break

print(answer)