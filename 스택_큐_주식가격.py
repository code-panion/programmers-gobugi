def solution(prices):
    answer = []
    crack=False
    # print(len(prices),"len(prices)")
    for i in range(len(prices)):
        time=0
        for j in range(i+1,len(prices)):
            if prices[i]<=prices[j]:
                # print(prices[i],prices[j],"i,j")
                time+=1
            else:
                # print(prices[i],prices[j],"i,j")
                time+=1
                break
        answer.append(time)
    # print(answer)
    return answer