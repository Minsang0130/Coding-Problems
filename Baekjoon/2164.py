# 1~N까지의 숫자
# 맨위 날리고 맨위에 있는 숫자를 맨 밑으로
# 마지막 한장 남을때까지
from collections import deque

N = int(input())

q = deque()

for i in range(1, N+1):
    q.append(i)

while len(q) != 1:
    q.popleft()
    num = q.popleft()
    q.append(num)

print(q[0])