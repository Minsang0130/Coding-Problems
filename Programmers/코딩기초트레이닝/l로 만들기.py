def solution(myString):
    for ch in myString:
        if ch < 'l':
            myString = myString.replace(ch, 'l')
    return myString