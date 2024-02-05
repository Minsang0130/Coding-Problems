def solution(code):
    mode = 0
    ret = ''
    for idx in range(0,len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx%2 ==0:
                    ret+= code[idx]
            elif code[idx]== '1':
                mode = 1
        elif mode ==1:
            if code[idx] != '1':
                if idx %2 != 0:
                    ret+= code[idx]
            elif code[idx] == '1':
                mode = 0
                    
            
    return ret if ret!='' else "EMPTY"

print(solution('abc1abc1abc'))