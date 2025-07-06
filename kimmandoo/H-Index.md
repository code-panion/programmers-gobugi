# 접근 방식
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

이 문장이 너무 헷갈렸다.
그래서 일단 오름 차순으로 정렬해서, 해당 idx에서 남은 리스트 개수와, 인용값을 비교해서 하나씩 순회하는 방향으로 설계했다.

```java
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int n = citations.length;
        Arrays.sort(citations);
        int h = 0;
        for(int i=1; i<=n; i++){
            // i번째 논문의 인용 수 체크 1-based
            int cit = citations[i-1];
            // 인용된 논문이 h편 이상인가?
            if(n-i+1 >= h){
                // 남은 논문 개수가 현재 인용 수 보다 크거나 같으면 성립
                h = cit;
            }
        }
        
        return h;
    }
}
```

내 코드의 문제는. h의 정의를 엄밀하게 못한다는 것이다.
cit이 n - i + 1보다 크거나 같을 때 그게 유효한 h 값 후보가 된다. 즉 인용 수가 인용된 논문 수 이상인 시점이 정답이다.


# 학습 내용

문제에서 제시한 조건인 h가 뭔지를 먼저 인지하고 가야한다. 현재 논문의 인용횟수가(정렬된 상태이므로) 남은 논문 편수들 보다 크거나 같아지면 끝난다. 인용된 횟수보다 남은 논문 편수에 의미가 있다.

# 풀이 코드 

```java
import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int n = citations.length;
        Arrays.sort(citations);
        
        for (int i = 0; i < n; i++) {
            int h = n - i; // 남은 논문 개수
            if (citations[i] >= h) {
                return h;
            }
        }
        
        return 0;
    }
}
```