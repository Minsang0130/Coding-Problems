def solution(myStr):
    myStr = myStr.replace('a', ' ')
    myStr = myStr.replace('b', ' ')
    myStr = myStr.replace('c', ' ')
    myStr = myStr.split()
    if myStr:
        return myStr
    else:
        return ["EMPTY"]