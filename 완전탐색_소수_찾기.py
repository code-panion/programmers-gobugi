# 만들 수 있는 모든 수를 만들고 소수 검증하기
# 숫자 길이가 고정되어 있지않은 것에 주의,
# for문 + 재귀하되 set 사용? => 중복 검증하니 새로운 수 모두 추가하기
# 대신 길이로 돌아갈 포인트 설정
# pos 리스트로 중복 검증하기
# 첫 숫자는 0이 될 수 없음 숫자 길이 & 0 체크

tot = []
def solution(numbers):
    global tot
    print(len(numbers))
    cur_num = []
    position = [0] * len(numbers)
    answer = 0
    leng=get_decimal(numbers,cur_num, position)
    
    tot = list(set(tot))
    # print(tot,'tot')
    for each in tot:
        # print(each,type(each))
        if each =='1':
            continue
        flg=True
        for indx in range(2,int(int(each)/2)+1):
            # print(indx)
            # print(indx,int(each),int(each)%indx,'int(each)%indx')
            if int(each)%indx == 0:
                flg=False
                break
        if flg:
            answer+=1
    # for each in 
    
    return answer

def get_decimal(numbers,num,pos):
    # print(num,numbers,len(num),len(numbers))

    if num and num[0]=='0':
        return
    
    if len(num)==len(numbers):
        tot.append(''.join(i for i in num))
        # print('hi')
        return

    if len(num)!=0:
        tot.append(''.join(i for i in num))
        
    for idx in range(len(numbers)):
        if pos[idx] == 0:
            pos[idx]=1
            num.append(numbers[idx])
            get_decimal(numbers,num,pos)
            num.pop()
            pos[idx]=0
    return
    
    