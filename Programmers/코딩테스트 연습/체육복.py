def solution(n, lost, reserve):
    lost = sorted(lost[:])
    reserve = sorted(reserve[:])
    
    keep = []
    for r in reserve:
        if r in lost:
            lost.remove(r)
        else:
            keep.append(r)

    for r in keep:
        if (r - 1) in lost:
            lost.remove(r - 1)
            continue
        if (r + 1) in lost:
            lost.remove(r + 1)
            continue

    return n - len(lost)
