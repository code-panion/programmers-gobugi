

def solution(k, dungeons):
    global leng
    global mx
    
    visited = [0]*len(dungeons)
    leng = len(dungeons)
    
    
    mx=0
    answer = -1
    # 피로도랑 던전수 가진다
    # 각 던전 하나씩 방문하고 피로도가 부족하면 백
    # 각각 최대수에서 +1
    checker=[]
    energy = k
    ans = make(energy, dungeons,checker,visited)
    # if ans == none:
    
    # print(mx,ans,"mx,ans")
    return ans

def make(enrgy,dungeons,check,visit):
    global mx
    global leng
    # print(enrgy,dungeons,check,visit, "enrgy,dungeons,check,visit")
    # print(len(check),leng,mx,"len check, leng mx")
    if len(check) == leng:
        mx = leng
        return
    if mx < len(check):
        mx = len(check)
    for i in range(len(dungeons)):
        if enrgy >= dungeons[i][0] and visit[i]==0:
            visit[i]=1
            check.append(dungeons[i][0])
            make(enrgy - dungeons[i][1],dungeons,check,visit)
            visit[i]=0
            check.pop()
            
        else:
            continue
    return mx
     