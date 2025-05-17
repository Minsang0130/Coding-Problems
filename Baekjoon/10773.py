from collections import deque
import sys

K = int(sys.stdin.readline())
q = deque()

for i in range(K):
    num = int(input())
    if num == 0:
        q.pop()
    else:
        q.append(num)

print(sum(q))