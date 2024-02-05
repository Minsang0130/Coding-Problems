import sys
input = sys.stdin.readline

basket_num, num = map(int, input().split())
basket_list = list(range(1,basket_num + 1))

for i in range(num):
    j, k = map(int, input().split())
    while True:
        if k - j >= 1:
            # print(j,k)
            basket_list[j-1], basket_list[k-1] = basket_list[k-1], basket_list[j-1]
            j += 1
            k -= 1
        else:
            break
        
for i in range(len(basket_list)):
    print(basket_list[i] ,end=' ')