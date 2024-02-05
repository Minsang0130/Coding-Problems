num = int(input())
num_list = list(map(int, input().split()))
find_num = int(input())
sum = 0
for i in range(num):
    if num_list[i] == find_num:
        sum += 1

print(sum)