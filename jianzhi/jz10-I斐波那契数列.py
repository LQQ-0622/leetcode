class Solution:
    # 动态规划
    def fib1(self, n: int) -> int:
        MOD = 10 ** 9 + 1
        if n < 2:
            return n
        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p = q
            q = r
            r = (p + q) % MOD
        return r

    # 矩阵快速幂
    def fib2(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n

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

        res = matrix_pow([[1, 1], [1, 0]], n - 1)
        return res[0][0]


result = Solution().fib2(5)
print(result)
