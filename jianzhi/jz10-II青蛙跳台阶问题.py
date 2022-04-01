class Solution:
    # 动态规划
    def fib1(self, n: int) -> int:
        MOD = 10 ** 9 + 1
        if n < 2:
            return 1  # 区别佩波纳契数列
        p, q, r = 1, 1, 1  # 区别佩波纳契数列
        for i in range(2, n + 1):
            p = q
            q = r
            r = (p + q) % MOD
        return r

    # 矩阵快速幂
    def fib2(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return 1

        def multiply(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:  # 矩阵相乘
            c = [[0, 0], [0, 0]]
            for i in range(2):
                for j in range(2):
                    c[i][j] = (a[i][0] * b[0][j] + a[i][1] * b[1][j]) % MOD
            return c

        def matrix_pow(a: list[list[int]], n: int) -> list[list[int]]:
            ret = [[1, 0], [0, 1]]
            while n > 0:
                if n & 1:
                    ret = multiply(ret, a)
                n >>= 1
                a = multiply(a, a)  # !
            return ret

        res = matrix_pow([[1, 1], [1, 0]], n)  # 因为f(0)=f(1)=1, 所以比佩波纳契数列多1
        return res[0][0]


result = Solution().fib2(7)
print(result)
