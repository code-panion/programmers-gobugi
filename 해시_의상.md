# 딕셔너리 새로 학습
# dict = {} 튜플 등 고정형 키 값을 사용
# i[item_name]=value으로 딕셔너리에 새 키 추가 (새로 값 지정해주며 추가)


# def dfs 방식으로 풀어보았으나 시간 문제(2시간) + 오류로 포기,
# 접근 방식이 지나치게 복잡했음
# 내 접근 방식 : 모든 입은 영우의 수를 dfs로 구하자
# 풀이 : 입은 수 + 안입은 수 = n+1이니 모든 종류별 개수를 for로 곱하고 모두 안입은 경우 하나를 뺴면 끝


def solution(clothes):
    answer = 0
    nw = {}
    for i in clothes:
        #if i[1] in nw:
        print(i[1])
        if i[1] in nw:
            nw[i[1]]+=1
        else:
            nw[i[1]]=1
        # nw[i[1]]=nw.get(i,0)+1
    numbers=[]
    for i in nw:
        # +1은 해당 종류의 옷을 안입는 케이스
        numbers.append(nw[i]+1)
    # print(numbers)
    tot = 1
    for cases in numbers:
        tot *= cases
    answer = tot-1
    return answer
    
        # for i in nw:
        # dfs?
        # cur=[]
        # nw 딕셔너리(키 가져올 것), 현재 포함한 옷 종류, 총 종류 total은 global 변수로
        # 종류별이니 리스트에서 순서대로 가져와서 종류 만들고 겹치지 않게 개수 모두 곱해서 종류 확인
        # 동일성 구분은 인덱스로, 리스트에 인덱스 보관, 전체 개수는 total에 바로 더하기
#     current=[]
#     mtltiple=1
#     dfs(numbers,current,mtltiple)
        
#         # len(nw),total, nw, cur
        
#     print(nw)
    
#     return answer
# 각 옷 종류별로 전체 가지수 만들면서 종류 확보
# 각 종류별 개수 서로 곱해서 더한다, 일단 리스트로 더해주고 나중에 sum
# 어떤 옷인지 확인하고 총 개수 따로 더한다?

# 확인한 옷 종류를 따로 리스트로 만들고 mul을 직접 곱하고 나누다보니 divide by 0등 오류발생

# gpt 코드를 보면 사용 인덱스, 깊이를 인자로 가져가고 곱해진 수도 mul로 함수에서 바로 곱해서 가져가니 다시 나눠줄 이유 없음, 재귀함수에 바로 넣는 것을 더 고려하고 사용성 확인을 인덱스로만 할 이유가 없음(물론 이 케이스는 앞의 경우를 사용 안하는 특수 케이스)




# 내 dfs 코드 (미완)
# def dfs(nums,cur,mul):
    
#     global total
    
#     if len(cur)==len(nums):
#         return
#     # idx, i in enumerate(nums):
#     if cur:
#         for idx in range(cur[-1],len(nums)):
#             total+=mul*nums[idx]
#             cur.append(idx)
#             dfs(nums,cur.mul)
#             mul/(cur.pop())
            
#     else:
#         for idx in range(len(nums)):
#             total=1
        
#             cur.append(idx)
#             dfs(nums,cur,mul)
#             mul/(cur.pop())




# gpt의 dfs 코드

# def solution(clothes):
#     global total
#     total = 0
    
#     kind_count = {}
#     for item in clothes:
#         kind = item[1]
#         kind_count[kind] = kind_count.get(kind, 0) + 1

#     numbers = list(kind_count.values())

#     dfs(numbers, 0, 0, 1)  # start: idx=0, depth=0, mul=1
#     return total

# def dfs(nums, idx, depth, mul):
#     global total
#     if depth > 0:
#         total += mul  # 최소 1개 이상 선택한 조합만 포함

#     for i in range(idx, len(nums)):
#         dfs(nums, i + 1, depth + 1, mul * nums[i])