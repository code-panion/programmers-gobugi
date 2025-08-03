def solution(arr):
    answer = []
    prev = -1
    for i in arr:
        if i == prev:
            continue
        else:
            answer.append(i)
            prev=i
    return answer