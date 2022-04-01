class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result = []
        minRow = [min(row) for row in matrix]
        maxCol = [max(col) for col in zip(*matrix)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == minRow[i] == maxCol[j]:
                    result.append(x)
        return result

    # 当知道幸运数最多只有一个，且行最小的最大值和列最大的最小值一样时，则为该值。
    def luckyNumbers1(self, matrix: list[list[int]]) -> list[int]:
        return [a] if (a := max(min(m) for m in matrix)) == (b := min(max(m) for m in zip(*matrix))) else []


matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
result = Solution().luckyNumbers(matrix)
print(result)
