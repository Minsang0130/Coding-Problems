basket, num = map(int, input().split())
basket_list = [0] * basket
# print(basket, num, len(basket_list))
for q in range(num):
    i, j, k = map(int, input().split())
    for basket_num in range(i,j+1):
        basket_list[basket_num - 1] = k

for i in range(len(basket_list)):
    print(basket_list[i], end=" ")