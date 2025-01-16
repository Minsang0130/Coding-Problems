def solution(age):
    age_dict = { '0' : 'a', '1' : 'b', '2' : 'c', '3' : 'd', '4' : 'e', '5' :'f', '6' : 'g', '7' : 'h', '8' :'i', '9' : 'j'}
    result = ''
    for ch in str(age):
        result += age_dict[ch]
    return result