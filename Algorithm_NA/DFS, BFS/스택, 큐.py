# 스택
stack = []
stack.append('x')
stack.append('y')
stack.append('z')
stack.pop()
print(stack) # 최하단 원소부터 출력 - x, y
print(stack[::-1]) # 최상단 원소부터 출력 y, x

# 큐
from collections import deque
queue = deque()
queue.append('x')
queue.append('y')
queue.append('z')
queue.popleft()
print(queue)  # 먼저 들어온 순서대로 출력 - y, z

queue.reverse()
print(queue) # 나중에 들어온 순서대로 출력 - z, y

list(queue) # 를 통해 파이썬 리스트 객체로 변환할 수 있다.
