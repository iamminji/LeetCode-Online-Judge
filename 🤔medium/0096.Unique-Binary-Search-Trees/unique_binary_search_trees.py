# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/


class Solution:

    # n개의 유니크한 binary search tree 를 만들 때 만들 수 있는 모든 경우의 수를 리턴하는 문제다.
    # 트리를 만드는 경우의 수는 이전 트리에 영향을 받으므로 dp로 풀 수 있다.
    def numTrees(self, n: int) -> int:

        if n < 0:
            return 0
        elif n <= 1:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        # 루트 가 3 인 경우는
        # 1이 루트인 경우 + 2가 루트인 경우 + 3이 루트인 경우를 합산한 것과 같다.
        # 이 때 트리 형태는 아래처럼 트리 노드로 이루어질 것이다.
        # 1이 루트라면 좌측 트리엔 0개 우측 트리엔 2개
        # 2가 루트라면 좌측 트리에 1개 우측 트리엔 1개
        # 3이 루트라면 좌측 트리에 2개 우측 트리엔 0개
        """
           1         3     3      2      1      
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3
                
        """

        # 4가 루트인 경우 역시
        # 1이 루트인 경우 + 2가 루트인 경우 + 3이 루트인 경우 + 4가 루트인 경우다.
        # 1이 루트일 때 (좌0, 우3) => 좌측에 0개 노드를 가진 트리를 만드는 방법 * 우측에 3개 노드를 가진 트리를 만드는 방법 => 1 * 5 = 5
        # 2이 루트일 때 (좌1, 우2) = 2
        # 3이 루트일 때 (좌2, 우1) = 2
        # 4이 루트일 때 (좌3, 우0) = 5
        # 좌와 우의 합이 n이 루트일때 n-1이 되는 이유는 부모 노드의 좌측 자식 노드가 부모 보다 작아야 하고 우측 자식 노드는 커야 되기 때문이다.

        # 결국 n 이 루트인 경우의 수는
        # 좌측 트리의 노드 * 우측 트리의 노드 조합이다.
        # 이 때, 0개의 노드로 이루어지는 경우는 결국 한 가지 방법 이므로 노드 0개를 가짓수 1로 보고

        # 공식으로 정리하자면
        # f(n) = f(0) * f(n-1) + f(1) * f(n-2) + f(2) * f(n-3) + ... + f(n-1) * f(0) 이 된다.

        # f(x) 는 x 개수의 unique 한 트리를 만드는 가짓수가 된다.
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(3))
    print(sol.numTrees(4))
