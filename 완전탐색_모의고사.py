def solution(answers):
    # 각 사용자 1명씩 전체 답안만큼 확인
    # 각 사용자 미중복 답안 작성
    # 전체 순서 돌면서 정답과 사용자 답안 비교
    # 각 사용자별 정답수 확인, 비교
    
    
    
    lst1=[1, 2, 3, 4, 5]
    lst2=[2, 1, 2, 3, 2, 4, 2, 5]
    lst3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    ans1=0
    ans2=0
    ans3=0
    
    for i, n in enumerate(answers):
        if n==lst1[i%len(lst1)]:
            ans1+=1
        if n==lst2[i%len(lst2)]:
            ans2+=1
        if n==lst3[i%len(lst3)]:
            ans3+=1

    # for leng in range(answers):
    comp = max(ans1,ans2,ans3)
    
    
    answer = []
    if ans1==comp:
        answer.append(1)
    if ans2==comp:
        answer.append(2)
    if ans3==comp:
        answer.append(3)
    
    return answer