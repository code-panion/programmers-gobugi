# kv 자료구조 코드 참고 후 풀이 

def solution(participant, completion):
    all={}
    
    for name in participant:
        if name in all:
            all[name]+=1
        else:
            all[name]=1
    for name in completion:
        if name in all:
            all[name]-=1
        else:
            # all[name]=1
            continue
    for i in all:
        if all[i]==1:
            answer=i
            print(i)
    # print(new)
    
    # for n in completion:
    #     seen.append(new[n])
        # print(num)
    
    # for go in range(len(participant)):
    #     if go in seen:
    #         continue
    #     else:
    #         # print(go,'go')
    #         answer=participant[go]
    #         # answer.join(...)은 join한 결과를 반환할 뿐, answer를 바꾸지 않아요.
    #         # answer.join(cparticipant[go])
    #         # answer.join(participant[go])
    #         # nofin.append(participant[go])
    # # print(nofin)
            
    return answer