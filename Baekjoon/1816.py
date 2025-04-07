tc = int(input())

for _ in range(tc):
    n = int(input())
    for num in range(2, 1000001):
        if n % num == 0:
            print("No")
            break
        if num == 1000000:
            print("Yes")
