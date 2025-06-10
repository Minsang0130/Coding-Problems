import heapq
import sys

def main():
    N = int(sys.stdin.readline())
    h_list = []

    for _ in range(N):
        n = int(sys.stdin.readline())
        if n == 0 and h_list:
            print(heapq.heappop(h_list))
        elif n > 0:
            heapq.heappush(h_list, n)
        else:
            print(0)

if __name__ == "__main__":
    main()