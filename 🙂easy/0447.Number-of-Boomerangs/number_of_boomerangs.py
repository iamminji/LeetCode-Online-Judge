# 447. Number of Boomerangs
# https://leetcode.com/problems/number-of-boomerangs/


from collections import defaultdict


class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for p in points:
            x, y = p[0], p[1]
            count_list = defaultdict(int)
            for q in points:
                x2, y2 = q[0], q[1]
                if x == x2 and y == y2: continue
                length = get_length(x, x2, y, y2)
                count_list[length] += 1
            for k, v in count_list.items():
                count += permutation(v)

        return count


def permutation(v):
    if v == 2: return 2
    return v * (v - 1)


def get_length(x, x2, y, y2):
    return (x - x2) ** 2 + (y - y2) ** 2


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
    print(sol.numberOfBoomerangs([[1, 1], [1, 2]]))
    print(sol.numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]))
