import sys
input = sys.stdin.readline
student_num = list(range(1,31))

for i in range(28):
    num = int(input())
    student_num.remove(num)

for i in range(len(student_num)):
    print(student_num[i])