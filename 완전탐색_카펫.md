def solution(brown, yellow):
    answer = []
    
    # special thanks to 권오윤 for 새로운 접근
    # 반으로 잘라 내부 외부 개수 세기

    # 1 = 8 => horizontal 3, vertical 1 each
    # 2 = 10 => horizontal 4 vertical 1 each
    # 3 = 12 => horizontal 5 vertical 1 each
    # 4 = 12 => horizontal 4 vertical 2 each
    # 5 = 16 => horizontal 7 vertical 1 each
    
    
    # 2 = 10 => horizontal 4 vertical 1 each => 2x1
    # 4 = 12 => horizontal 4 vertical 2 each => 2z2
    # 6 = 14 => horizontal 5 vertical 2 each => 3x2
    # horizontal = n +2, vertical = 1 each
    
    # 1 = 8 => horizontal 3, vertical 1 each => 1x1
    # 3 = 12 => horizontal 5 vertical 1 each => 3x1
    # 5 = 16 => horizontal 7 vertical 1 each => 5x1
    
    # 9 => 3x3, 16
    # horizontal = n +2, vertical = 1 each
    
    # 24 => 4x6
    
    # 35 => 5x7 => 7x9
    
    # 45 = 1,3,5,9,15,45
    # 24 = 1,2,3,4,6,8,12,24
    # 9 => 1,3,9
    
    # 28 => 1,2,4,7,14,28
    
    # 1,2,3,6,12,18,36
    
    # 약수를 싹다 구하고 중간값 자리의 두개를 추출, 각각 +2씩한다
    
    # print(yellow)
    lst = []
    # print(yellow//2+1,"yellow//2+1")
    for i in range(1,yellow//2+1):
        if yellow%i==0:
            lst.append(i)
        else:
            continue
    lst.append(yellow)
    # lst = 약수들
    point=int(len(lst)//2)
    # if yellow%2!=0: # 제곱수
    
    # 노란 네모들이 하나의 형태가 아닐수도 있다!
    # if len(lst)%2!=0:
    #     answer=[lst[point]+2,lst[point]+2]
    # else:
    #     answer=[lst[point]+2,lst[point-1]+2]
    # print(lst,point)
    print(lst,"lst")
    for i in range(len(lst)//2+1):
        print(lst[i],"lst[i]",lst[len(lst)-1-i],"lst[len(lst)-1-i]")
        if lst[i] != lst[len(lst)-1-i]:
            if 2*(lst[i]+2)+2*(lst[len(lst)-1-i])==brown: # 4, 14
                if lst[i]+2>=lst[len(lst)-1-i]+2:
                    answer=[lst[i]+2,lst[len(lst)-1-i]+2]
                else:
                    answer=[lst[len(lst)-1-i]+2,lst[i]+2]
            else:
                continue
        else:
            print(2*(2*(lst[i])+2),"2*(lst[i]+2)")
            if brown == 2*(2*(lst[i])+2):
                answer=[lst[i]+2,lst[i]+2]
            else:
                continue
    
    return answer