# 각 수별로 +- 해봐야함 (완탐)
# 각 위치별로 +- 수행 (dfs)
# 연산 후 target과 맞는지 확인, 맞다면 개수 업데이트

ans=0

def solution(numbers, target):
    global ans
    answer = 0
    currently=[]
    answer = sign(numbers,currently,target)
    return ans

# 현재 부호 수 필요
def sign(num,curr,tgt):
    global ans
    
    # 다 찼으면 부호, 숫자 하나씩 꺼내서 연산
    if len(curr)==len(num):
        # print(curr,'curr, worked')
        tot=0
        for i in range(len(num)):
            if curr[i] == '+':
                tot+=num[i]
            else:
                tot-=num[i]
        if tot==tgt:
            ans+=1
        return
    cal=['+','-']
    for sgn in cal:
        curr.append(sgn)
        sign(num,curr,tgt)
        curr.pop()