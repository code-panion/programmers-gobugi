# genres plays idx 모두 사용
# 각 genre별 play 합으로 우선 정렬, 그다음 play의 연주별 정렬, 고유 번호는 dix
# 람다식 사용 필요, 복습
# .sort(lambda: lambda key=x?)
def solution(genres, plays):
    answer = []
    # 한번에 모아서 장르 / 연주 수로 정렬
    combine=[]
    # genre={"pop":[[500,1]],"classic":[150,2]}
    genre={}
    each_genre={}
    
    # 딕셔너리로 장르별 연주 회수 및 인덱스 정리
    # 딕셔너리로 장르별 총 연주 횟수 확인
    for idx in range(len(genres)):
        if genres[idx] in genre:
            genre[genres[idx]].append([plays[idx],idx])
            each_genre[genres[idx]]+=plays[idx]
        else:
            genre[genres[idx]]=[[plays[idx],idx]]
            each_genre[genres[idx]]=plays[idx]
    
    # print(genre)
    # print(each_genre)
    
    srt=[]
    
    # 전체 장르별 연주수 리스트로 변환
    for total_play in each_genre:
        srt.append([each_genre[total_play],total_play])
    # 정렬하여 가장 연주수 많은 장르부터 선별
    srt.sort(reverse=True)
    
    # print(srt)

    # 가장 연주수 많은 장르부터 꺼내어 연주수, 인덱스 별 정렬
    for i in srt:
        genre[i[1]].sort()
        # print(genre[i[1]])
        # print(genre[i[1]],'genre[i[1]]')
        
        if len(genre[i[1]])>1:
            if genre[i[1]][-1][0]==genre[i[1]][-2][0]:
                # print('crash')
                answer.append(genre[i[1]][-2][1])
                answer.append(genre[i[1]][-1][1])
                # answer.append(genre[i[1]][-2][1])
            else:
                answer.append(genre[i[1]][-1][1])
                answer.append(genre[i[1]][-2][1])
        else:
            answer.append(genre[i[1]][-1][1])
        
    
    # print(answer)

    return answer