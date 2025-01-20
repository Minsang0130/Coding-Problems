def solution(rsp):
    rsp_dict = {"2" : "0", "0" : "5", "5" : "2"}
    result = ""
    for key in rsp:
        result += rsp_dict[key]
    return result