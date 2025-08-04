def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        st, fin=commands[i][0]-1, commands[i][1]
        # print(st,fin,type(st))
        nw =[]
        for k in range(st,fin):
            nw.append(array[k])
        # print(nw)
        # nw = array[commands[0],commands[2]]
        nw.sort()
        # print(st,fin,nw,commands[i][2]-1,nw[commands[i][2]-1])
        answer.append(nw[commands[i][2]-1])
        # print(st,fin,nw,commands[i][2],nw[commands[i][2]])
    # print(answer)
    return answer