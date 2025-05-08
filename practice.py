#5248 그룹 나누기

# 부모노드 탐색 함수
def find_root(x):
    if x == p_lst[x]:
        return x ! 2

    else:
        p_lst[x]=find_root(p_lst[x])
        return p_lst[x]

# 합집합 함수
def union(x,y):
    px=find_root(x)
    py=find_root(y)

    if px >= py:
        p_lst[px]=py
    else:
        p_lst[py]=px


# main
T=int(input())
for tc in range(1,T+1):
    # N:노드 개수, M:쌍 개수, lst:입력 리스트, p_lst:루트노드 저장 리스트 
    N,M=map(int,input().split())
    lst=list(map(int,input().split()))
    p_lst=[0]*(N+1)

    # 부모노드 자기 자신으로 초기화
    for i in range(N+1):
        p_lst[i]=i

    # 그룹핑
    idx=0
    for _ in range(M):
        union(lst[idx],lst[idx+1])
        print(lst[idx], lst[idx+1])
        print(p_lst)
        idx+=2

    # 결국 원하는건 그룹의 개수
    # 그룹의 개수 => 대표자의 개수
    for i in range(1, N+1):
        p_lst[i] = find_root(i)

    # 자신 인덱스가 부모 노드값이라면, 루트이므로 cnt+1
    cnt=0
    for i in range(1,N+1):
        if i==p_lst[i]:
            cnt+=1
        

    print('부모 리스트 결과',p_lst)
    #print(f'#{tc}',cnt)