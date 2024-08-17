def solution(my_string):
    num_list = [0 for i in range(52)]
    alphabet_1 = range(65,91)
    alphabet_2 = range(97,123)
    alphabet = list(alphabet_1) + list(alphabet_2)
    for i in my_string:
        for j in range(0,len(alphabet)):
            if ord(i) == alphabet[j]:
                num_list[j] += 1
    return num_list
