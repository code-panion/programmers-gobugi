# 가장 큰 수부터 앞에 넣는다
# 두자리 수는 첫 자리 비교 후 둘째자리 따로 비교한다? -> 1000은?
# 각 자리수 따로 비교해야함
# 앞자리부터 따로 또 정렬 -> 어떻게?
# 문자열로 자리수 정렬한다 -> how? 문자열은 각 자리별 수로 비교!
# 919191,999면 919191의 경우 첫자리 9, 둘째 자리 1, 999는 첫자리 9, 둘째자리 9
# 따라서 999가 더 크다 => 입력 숫자 길이 중 가장 긴 자리수를 기준으로 곱하여 주면 된다!


def solution(numbers):
    new = []
    # print(numbers)
    leng =  len(str(max(numbers)))
    k=True
    for i in range(len(numbers)):
        if numbers[i] != 0:
            k = False
        # print(numbers[i])
        new.append([str(numbers[i])*leng,len(str(numbers[i]))])
    if k==False:
        new.sort(reverse=True)
        num=''
        for i in new:
            # print(i[0][:i[1]],i[1])
            num+=i[0][:i[1]]
    else:
        num='0'
    # print(new)
    # numbers.sort()
    # ans = ''
    # for i in range(numbers):
    # for num in numbers:
    #     print(num)
        # ans += str(num)
    
    return num

# 재귀 풀이

# 전체 리스트를 받고
# 하나씩 붙여야함
# 숫자 순서별로 하나씩 문자로 전부 붙여서 수를 만들고 이때 중복이 없어야함
# 그리고 문자이므로 숫자로 바꾸고 가장 큰 수를 만든다
# 전체 리스트에 넣고 가장 큰 수 뽑아도 ㄱㅊ 혹은 가장 큰 수 인지 계속 비교
# 중복 피할려면 위치 인덱스 추가

# 문제 : 각 리스트에서 하나씩 다 꺼내서 수 만들기

# sys.setrecursionlimit(109)
# mx = -1

# def solution(numbers):
#     # mx는 숫자로 비교한 다음 마지막에 문자열로 반환
#     global mx
#     # print(mx)
    
#     cur_num = []
#     ps = [0] * len(numbers)
#     # tst=['3','5']
#     # a = int(''.join(i for i in tst))
#     # print(a)
#     ans = dfs(numbers,cur_num,ps)
    
#     # 정답은 문자열로 반환!
#     return str(mx)


# def dfs (total,num,pos):
#     global mx
#     if len(num)==len(total):
#         new = str(''.join(str(i) for i in num))
#         if mx < int(new):
#             mx = int(new)
#         # print(new)
#         # 리스트에서 숫자로
#         # 가장 큰 숫자 찾기
#         return
#     for nxt in range(len(total)):
#         if pos[nxt]==0:
#             pos[nxt]=1
#             num.append(total[nxt])
#             dfs(total,num,pos)
#             pos[nxt]=0
#             num.pop()
#         else:
#             continue
    
#     return