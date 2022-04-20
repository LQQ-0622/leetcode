class Solution:
    def rotate_offical(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]

    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def rotate_nums(this_positions: list[
            list[int]]):  # this_positions此位置的值覆盖next_positions下一个位置的值，返回覆盖this_position此位置的pre_positions位置
            pre_positions = []
            for this_position in this_positions:
                pre_position = [n - 1 - this_position[1], this_position[0]]
                next_position = [this_position[1], n - 1 - this_position[0]]
                matrix[next_position[0]][next_position[1]] = matrix[this_position[0]][this_position[1]]
                pre_positions.append(pre_position[:])
            return pre_positions

        start, stop = 0, n
        while start < stop - 1:
            first = []  # 记录此圈上方的值（第四次旋转放在右边的值）
            for i in range(start, stop - 1):
                first.append(matrix[start][i])

            this_positions = []
            for i in range(stop - 1, start, -1):  # 记录本次移动的位置
                this_positions.append([i, start])
            for i in range(3):  # 旋转三次
                this_positions = rotate_nums(this_positions)
            for position in this_positions:  # 最后一次旋转，将原矩阵上面放到右面
                next_position = [position[1], n - 1 - position[0]]
                matrix[next_position[0]][next_position[1]] = first[position[1] - start]
            start += 1
            stop -= 1


# input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
input = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# input = [[1]]
Solution().rotate1(input)
result = input
print(result)
