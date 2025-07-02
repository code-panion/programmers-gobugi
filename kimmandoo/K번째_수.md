# 접근 방식

부분 정렬정도가 그나마 문제였던 것 같다.
편하게 배열을 쓰려고 ArrayList를 사용했고, Collections.sort()로 정렬해서 쉽게 풀었다.
전역에 선언한 ArrayList는 clear로 매 loop마다 초기화 해줬음.

# 학습 내용
찾아보니, 부분배열을 꺼내와서 쓰는 방법이 있었다.
배열복사.
```java
int[] subArray = Arrays.copyOfRange(array, cmd[0]-1, cmd[1]);
Arrays.sort(subArray);
answer[idx++] = subArray[cmd[2]-1];
```
copyOfRange가 그건데, 원본 배열, 시작점, 종점으로 나뉘어져있고 범위는 `[, )` 이다.
메모리를 조금 덜 먹기 때문에 최후의 수단으로 알아둬야할 기술인 것 같다.


# 풀이 코드 
```java
import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> arr = new ArrayList();
        int[] answer = new int[commands.length];
        int idx = 0;
        for(int[] cmd: commands){
            // 정렬된 i부터 j번째 사이의 k번째 수
            for(int i=cmd[0]-1; i<cmd[1]; i++){
                arr.add(array[i]);
            }
            Collections.sort(arr);
            answer[idx++] = arr.get(cmd[2]-1);
            arr.clear();
        }
        
        return answer;
    }
}
```