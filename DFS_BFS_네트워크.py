# 자기 자신과 연결된 노드는 1로 표시
# 전체 노드 수 n
# 주어진 정보 기반으로 양방향 그래프 생성 혹은 각 리스트에 노드 번호 저장
# 각 노드별 연결된 노드 번호 저장 후 bfs로 순회 -> visited 사용, 전체 노드 순회

def solution(n, computers):
    answer = 0
    nodes = [[] for _ in range(n)]
    # print(nodes)
    
    # 주어진 정보 기반으로 양방향 그래프 생성 혹은 각 리스트에 노드 번호 저장
    for idx in range(n):
        for con_idx in range(n):
            if computers[idx][con_idx]==1: # and con_idx != idx:
                nodes[idx].append(con_idx)
    # print(nodes)
    
    visited = [0 for _ in range(n)]
    nw = [0 for _ in range(n)]
    network=0
    # 각 노드별 연결된 노드 번호 저장 후 bfs로 순회 -> visited 사용, 전체 노드 순회
    # print(visited,'before')
    ntw=0
    for nds_idx in range(n):
        ntw+=1
        # 각 인덱스 별로 bfs
        qu=[nds_idx]
            # nw=True
        while qu:
            st=qu.pop()
            # if visited[st]==True:
            #     break
            for nxt in nodes[st]:
                # print(nxt,visited[nxt],'nxt')
                if visited[nxt]==0:
                    visited[nxt]=ntw
                    qu.append(nxt)
                else:
                    continue
            # visited[st]=ntw
            # print(visited,'visted')
        # ntw+=1
    ans = 0
    comp=-1
    visited=list(set(visited))
    
    # 연속된 숫자만 같은 네트워크로 인식하여 틀림
    # 1,2,1 -> 네트워크 3개가 되버림
    
    # print(visited)
    # print(len(visited))
    # for to_comp in visited:
    #     if comp != to_comp:
    #         ans +=1
    #         comp=to_comp
    
    return len(visited)

# dfs인거 같은데?
# 각 연결된 노드 모두 연결하고 체크되어 있으면 패쓰하고?
