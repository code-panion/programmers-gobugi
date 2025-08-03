def solution(nums):
    answer = 0
    count=list(set(nums))
    total=len(nums)
    cnt=int(total/2)
    # count에서 cnt개 뽑아 최대 개수 만들기
    # ???? count pi cnt인가
    if len(count) >= cnt:
        answer=cnt
    else:
        answer=len(count)
    return answer