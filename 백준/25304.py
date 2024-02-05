money = float(input())
item_num = int(input())
sum = 0
for i in range(item_num):
    a, b = map(float, input().split())
    sum = sum + a * b

if sum == money:
    print("Yes")
else:
    print("No")