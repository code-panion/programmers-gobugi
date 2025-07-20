### 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42748

# 접근 방식
정렬이라서 문제에서 요구하는 데로 일단 해당 범위를 먼저 설정하고 범위 내에서 정렬 후 값을 리턴하도록 코드를 구현했다. 

</br>
</br>

# 학습내용
정렬을 sort를 쓰지 않고 구현해볼까 했는데 굳이 그래야 하나 싶어서 걍 sort 써도 통과했길래 그냥 풀었다. 난이도 1이라서 쉬어가는 문제인 걸로ㅎㅎ

</br>
</br>

# 풀이 코드

```
def sort(s, e, x, arr):
    #print(s,e,x, arr)
    data = []
    for i in range(s-1, e):
        data.append(arr[i])
    data.sort()
    return data[x-1]

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        v = sort(commands[i][0], commands[i][1], commands[i][2], array)
        answer.append(v)
    
    return answer
```

