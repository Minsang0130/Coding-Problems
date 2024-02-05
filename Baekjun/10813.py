basket_num, num = map(int, input().split())
basket_list = []
for i in range(basket_num):
    basket_list.append(i+1)

temp = 0

for i in range(num):
    i, j = map(int, input().split())
    temp = basket_list[i-1]
    basket_list[i-1] = basket_list[j-1]
    basket_list[j-1] = temp

for i in range(len(basket_list)):
    print(basket_list[i], end=" ")