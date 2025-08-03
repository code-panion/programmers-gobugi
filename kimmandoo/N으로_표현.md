# 접근방식

dp값을 정의할 때, dp[k] = N을 k번 사용해서 만들 수 있는 숫자들의 집합이라고 정의했다.

# 학습내용

이건 디피 분류중에 제일 어려웠 던 것 같다.
1. N을 k번 이어 붙인 수(예: k=3이면 555)를 k번째 Set에 추가
2. i + j = k가 되는 모든 (i, j) 조합에 대해 연산을 수행할 것 -> 하위 루프를 돌면서 j+ (i-j)가 i가되는 경우
3. i번째 Set에 있는 모든 숫자와 j번째 Set에 있는 모든 숫자를 가져옴
4. 두 숫자로 가능한 모든 사칙연산(+, -, *, /) 결과를 k번째 Set에 추가


# 풀이코드
```java
import java.util.*;

class Solution {
    public int solution(int N, int number) {
        if (N == number) {
            return 1;
        }

        List<Set<Integer>> dp = new ArrayList<>();
        for (int i = 0; i <= 8; i++) {
            dp.add(new HashSet<>());
        }

        // N을 1번 사용
        dp.get(1).add(N);

        for (int i = 2; i <= 8; i++) {
            dp.get(i).add(Integer.parseInt(String.valueOf(N).repeat(i)));

            for (int j = 1; j < i; j++) {
                Set<Integer> set1 = dp.get(j);
                Set<Integer> set2 = dp.get(i - j);

                for (int num1 : set1) {
                    for (int num2 : set2) {
                        dp.get(i).add(num1 + num2);
                        dp.get(i).add(num1 - num2);
                        dp.get(i).add(num1 * num2);
                        if (num2 != 0) {
                            dp.get(i).add(num1 / num2);
                        }
                    }
                }
            }

            if (dp.get(i).contains(number)) {
                return i;
            }
        }

        return -1;
    }
}
```