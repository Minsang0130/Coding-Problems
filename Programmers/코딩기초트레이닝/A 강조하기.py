def solution(myString):
    result = []
    myString = myString.replace('a', 'A')
    for ch in myString:
        if ch != 'A' and ch.isupper():
            result.append(ch.lower())
        else:
            result.append(ch)
    return ''.join(result)

sentence = "PrOgRaMmErS"
print(solution(sentence))