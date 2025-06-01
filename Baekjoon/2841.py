import sys

def main():
    N, P = map(int, sys.stdin.readline().split())
    guitar_list = [[] * P for _ in range(7)]
    count = 0

    for _ in range(N):
        n, p = map(int, sys.stdin.readline().split())
        while guitar_list[n] and guitar_list[n][-1] > p:
            guitar_list[n].pop()
            count += 1
        if not guitar_list[n] or guitar_list[n][-1] < p:
            guitar_list[n].append(p)
            count += 1

    print(count)

if __name__ == "__main__":
    main()