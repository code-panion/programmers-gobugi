### 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747

# 접근 방식
일단 h 값은 h개의 논문이 있어야 하기 때문에 최대 h 값을 list의 길이로 초기화와 선언한 다음 해당 조건을 만족하는지 확인하도록 했다.  

</br>
</br>

# 학습내용
x 번 인용된 논문이 몇개나 있는 지 확인하기 위한 quote 리스트를 만든 뒤 카운트 하도록 했다. 이때 인용되지 않은 것과 그냥 리스트에 아예 존재하지 않았던
숫자를 구분하기 위해 처음엔 -1로 값을 설정했다가 논문 인용횟수로 카운트되면 0이 되도록 했다. 그리고 맨 마지막 문제 하나만 시간 초과가 나길래 봤더니 
cnt 와 cnt2가 조건을 만족하지 못할 때 바로 끊어내는 가지치기가 없어서 추가했다. 

</br>
</br>

# 풀이 코드

```
def solution(citations):
    answer = 0
    quote = [-1] * 10001
    for i in range(len(citations)):
        if quote[citations[i]] == -1:
            quote[citations[i]] = 0
        quote[citations[i]] += 1
    max_h = len(citations)
    flg = False
    while not flg:
        cnt = 0
        cnt2 = 0
        #print(max_h)
        for k in range(max_h, 10001):
            if quote[k] and quote[k] != -1:
                cnt += quote[k]
        if max_h > cnt:
            max_h -= 1
            continue
        for k in range(0, max_h):
            if quote[k] and quote[k] != -1:
                cnt2 += quote[k]
        if max_h < cnt2:
            max_h -= 1
            continue
        elif max_h <= cnt and max_h >= cnt2:
            flg = True
            break
        max_h -= 1
    answer = max_h
    return answer
```

