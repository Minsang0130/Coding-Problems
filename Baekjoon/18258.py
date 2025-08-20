import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    q = [0] * N
    head = tail = size = 0
    out = []

    for _ in range(N):
        cmd_list = input().split()
        cmd = cmd_list[0]

        if cmd == "push":
            q[tail] = cmd_list[1]
            tail = (tail + 1) % N
            size += 1
        elif cmd == "pop":
            if size == 0:
                out.append("-1")
            else:
                out.append(q[head])
                head = (head + 1) % N
                size -= 1
        elif cmd == "size":
            out.append(str(size))
        elif cmd == "empty":
            if size == 0:
                out.append('1')
            else:
                out.append('0')
        elif cmd == 'front':
            if size == 0:
                out.append('-1')
            else:
                out.append(q[head])
        elif cmd == 'back':
            if size == 0:
                out.append('-1')
            else:
                out.append(q[(tail - 1) % N])

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
