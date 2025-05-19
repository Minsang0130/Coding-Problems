import sys
import ast
from collections import deque

def main():
    T = int(sys.stdin.readline())

    for tc in range(T):
        p_list = list(input())
        n = int(sys.stdin.readline())
        num_list = ast.literal_eval(sys.stdin.readline())
        dq = deque(num_list)
        reverse_flag = False

        # 주어진 수보다 삭제가 많으면 에러 리턴
        if p_list.count('D') > n:
            print("error")
            continue

        for p in p_list:
            if p == 'R':
                reverse_flag = not reverse_flag
            else:
                if reverse_flag:
                    dq.pop()
                else:
                    dq.popleft()

        if reverse_flag:
            dq.reverse()
        print(f"[{','.join(map(str, dq))}]")


if __name__ == "__main__":
    main()
