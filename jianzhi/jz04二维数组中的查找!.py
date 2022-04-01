class Solution:
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        if matrix == []: return False  # 考虑[]0情况
        row = len(matrix)
        col = len(matrix[0])
        row = len(matrix)
        col = len(matrix[0])
        # if 0 <= row <= 1000 & 0 <= col <= 1000:
        #     return -1
        i, j = 0, col - 1  # i:行, j:列
        while (i < row and j >= 0):
            # temp = matrix[i][j]
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
matrix = []
target = 5
found = Solution().findNumberIn2DArray(matrix, 5)
print(found)
