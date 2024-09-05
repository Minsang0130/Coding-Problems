def solution(todo_list, finished):
    result = []
    for idx, finished in enumerate(finished):
        if not finished :
            result.append(todo_list[idx])
    return result