## 문제 설명
정렬되어 있는 숫자 배열이 주어진다. 이 숫자 배열로 balanced tree 를 만들어서 리턴하는 문제다.

## 솔루션
문제의 핵심은 다음과 같다.

1. 이미 배열이 정렬되어 있다. 
2. balanced tree 의 조건으로 부모 노드 값 보다 작은 것이 좌측, 큰 것이 우측에 온다.

__또한, 문제에선 답이 여러개일 수도 있다고 했다__

배열이 정렬되어 있기 때문에 부모 노드는 전체 숫자 배열 중 가장 가운데 값이 오는 경우가 가장 문제 풀기가 쉽다.(?)
가운데 값을 (이하 mid) 늘 부모 노드로 오게 하고 mid 보다 작은 것을 좌측 (left) 큰 것을 우측 (right) 에 오게 하면 된다.

그리고 이 방식을 재귀로 계속 진행하면 된다.
