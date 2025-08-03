# 다리 위에는 이동한 시간과 무게 표시된 트럭들 기록
# 각 트럭별 시간 체크 후 다리에서 off
# 무게, 길이 적합성 확인 후 onboard

def solution(bridge_length, weight, truck_weights):
    # 전체 시간
    answer = 0
    # 건널 트럭 수
    tgt=len(truck_weights)
    # 남은 트럭들
    remain = truck_weights
    # 다리 위 트럭 수
    brdg = []
    # 지나간 트럭 수
    offed=0
    # print(truck_weights,"truck_weights")
    # print(len(brdg),bridge_length,"leng")
    
    # 새 트럭 
    new=truck_weights.pop(0)
    brdg.append([new,1])
    answer+=1
    print(len(brdg))
    
    
    while offed!=tgt:
    # for _ in range(10):
        # 각 트럭별 현재 위치 및 off, 전체 무게 측정
        off=False
        current_weight=0
        for on_truck in range(len(brdg)):
            # 건넜는지 다리 길이와 비교하여 확인
            if brdg[on_truck][1]==bridge_length:
                off=True
            else:
                # 아니라면 이동시간+1 & 무게 합산
                brdg[on_truck][1]+=1
                current_weight+=brdg[on_truck][0]
        # 맨 앞 트럭 위치 확인 후 off
        if off == True:
            brdg.pop(0)
            offed+=1
        # print(brdg,"after off board")
        # 마지막에 시간 1초 추가
        answer +=1
        # print(truck_weights,"truck_weights")
        # 만약 길이, 무게 된다면 onboard
        if truck_weights and len(brdg)<=bridge_length and current_weight+truck_weights[0]<=weight:
            new=truck_weights.pop(0)
            brdg.append([new,1])
        # # 만약 길이, 무게 된다면 onboard
        # if len(brdg)<=bridge_length and current_weight+truck_weights[0]<=weight and truck_weights:
            # print(truck_weights)
            # new=truck_weights.pop(0)
        #     brdg.append([new,1])
        # print(brdg, "after boarding")
    return answer