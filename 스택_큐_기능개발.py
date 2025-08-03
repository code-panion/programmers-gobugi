def solution(progresses, speeds):
    
    # find remaining days of each work and save it on new list 'ready'
    # from list, find a number that is bigger than start num and stop
    # numbers in front of it is num of work to deploy
    
    # make remain list
    ready=[]
    leng=len(progresses)
    for i in range(leng):
        remain = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i] != 0:
            remain+=1
        ready.append(remain)
    
    # find works to deploy together -> make answer
    start = 0
    together=0
    prev=ready[0]
    answer = []
    while start!=leng:
        if prev<ready[start]:
            answer.append(together)
            together=1
            prev=ready[start]
            start+=1
        else:
            together+=1
            start+=1
    # add final together num
    answer.append(together)
    
    print(answer)
    
    
    
    return answer