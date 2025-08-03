def solution(phone_book):
    answer = True
    prev='a'
    phone_book.sort()
    # print(phone_book)
    # 파이썬 사기, 수가 정렬되었으므로 그냥 앞수가 뒷수에 포함되는지 확인
    
    for num in phone_book:
        # 단순히 in으로 검사하면 65도 765안에 있어서 false 처리됨
        if prev in num:
            flg=True
            for i in range(len(prev)):
                if not prev[i]==num[i]:
                    flg=False
                    break
            if flg==True:
                answer=False
        else:
            prev=num
    
    # # 앞과 첫 수가 같으면 해당 수 첫 위치부터 지금까지 수 중 포함되는게 있는지 확인
    # for idx, num in enumerate(phone_book):
    #     if num[0]==prev:
    #         # 동일 시작 수 비교
    #         # print(num,prev)
    #         # 전 위치부터 현재 수 직전까지
    #         for i in range(prev_pos,idx): 
    #             if phone_book[i] in phone_book[idx]:
    #                 # print('gotcha')
    #                 answer=False
    #             else:
    #                 continue
    #     else:
    #         # print(num,prev,'change')
    #         prev=num[0]
    #         prev_idx=idx
    return answer