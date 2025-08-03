def solution(priorities, location):

   # shout out to 권오윤 for help!

#     mx_num = max(priorities)
#     num = priorities[location]
#     if mx_num == num:
#         answer=0
#     else:
#         answer=1
    
#     flg = False
#     length=len(priorities)
#     for i in range(length):
#         if priorities[i]==mx_num:
#             print(priorities[i], mx_num, "priorities[i]==mx_num")
#             flg=True
#             answer+=1
#         elif priorities[i]>=num and flg==True:
#             answer+=1
#         else:
#             continue
#         print(i, flg, answer, "i,flg, answer")

#     answer = 1
#     # 최댓값 위치 찾기, 위치 값 찾기
#     # 최댓값이 아니라면, 최댓값 뒤 숫자 개수가 중요
#     # 위치 값과 동일한 값은 최댓값 뒤 개수, 그 외는 위치 값보다 큰 수의 개수 찾기
#     # num = priorities[location]
#     lst=[]
    
#     for i in range(len(priorities)):
#         lst.append(i+1)
#     num = lst[location]
#     ans=[]
    
    
#     process = True
#     # while process:
#     for i in range(5):
#         if priorities:
#             mx = max(priorities)
#         print(priorities, lst, "priorities", "lst","before")
#         if priorities[0]!=mx:
#             last= priorities.pop(0)
#             priorities.append(last)

#             last_num=lst.pop(0)
#             print(num,last_num)
#             if num == last_num:
#                 process = False
#             else:
#                 lst.append(last_num)
#                 # answer+=1
#             print(priorities, lst, "priorities", "lst","after")
#         else:
#             last= priorities.pop(0)
#             last_num=lst.pop(0)
#             ans.append(last_num)
        
#         for i in range(len(ans)):
#            if ans[i]==num:
#                break
#            else:
#                answer += 1
#         print(len(ans))
    
    lst=[]
    answer=0
    for i in range(len(priorities)):
        lst.append(i)
    
    mx_num = max(priorities)

    nm_pos = lst[location]

    # for i in range()
    # 우선순위, 위치 마킹 리스트 생성
    # 최댓값 위치구하고
    # 우선순위 최댓값이 두 리스트의 가장 앞으로 가도록 정렬
    # 차례로 마킹리스트보다 크면 answer+1
    ans=[]
    while priorities:
        mx=max(priorities)
        pos=lst.pop(0)
        pri=priorities.pop(0)
        
        if pri == mx:
            ans.append(pos)
        else:
            lst.append(pos)
            priorities.append(pri)
    print(ans)
    for i in range(len(ans)):
        if location==ans[i]:
            answer=i
            break
    
    return answer+1



