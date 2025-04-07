def solution(dots):
    x_values = [x for x, y in dots]
    y_values = [y for x, y in dots]
    
    width = max(x_values) - min(x_values)
    height = max(y_values) - min(y_values)
    
    return width * height
