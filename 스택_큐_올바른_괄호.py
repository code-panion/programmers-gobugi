def solution(s):
    answer = True
    q=0
    for i in s:
        if i=='(':
            q+=1
        else:
            q-=1
        if q<0:
            answer=False
            break
    if q!=0:
        answer=False

    return answer