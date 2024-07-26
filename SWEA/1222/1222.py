import sys
sys.stdin = open('input.txt', 'r')

def postfix_natation_plus(string_num, arr):
    result = []
    for i in range(len(arr)):
        if arr[i] >= '0' and arr[i] <= '9':
            result.append(arr[i])
        elif arr[i] == '+' and len(result) > 1:
            num1 = int(result.pop())
            num2 = int(result.pop())
            result.append(num1 + num2)
    return result[0] + int(arr[len(arr)-1])

def postfix_natation(string_num, arr):

    def stack_push(i):


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):

    # def peek(self):

for test_case in range(1, 11):
    n = int(input())
    input_str = list(input())
    print(f'#{test_case} {postfix_natation_plus(n, input_str)}')
