def solution(sizes):
    print(sizes)
    
    mx_r = 0
    mx_l = 0
    for row in sizes:
        temp = 0
        if row[0]<row[1]:
            temp=row[0]
            row[0]=row[1]
            row[1]=temp
        if row[0] > mx_r:
            mx_r=row[0]
        if row[1] > mx_l:
            mx_l=row[1]
    
    answer = mx_r*mx_l
    return answer

# 받고
# 가장 긴게 어느쪽인지 확인
# 좌 우 중 긴게 어디인지 체크하고
# 가장 긴쪽에 맞게 긴쪽들 모두 정렬
# 그다음 각 좌 우에서 가장 긴 수 곱하기

