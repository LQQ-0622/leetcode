class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')
        res = list(s)
        res.extend([' '] * counter * 2)  # 扩展列表
        left, right = len(s) - 1, len(res) - 1
        while not left == right:
            if res[left] != ' ':
                res[right] = res[left]
                right -= 1
            else:
                res[right - 2: right + 1] = '%20'   # 左闭右开
                right -= 3
            left -= 1
        return ''.join(res)


a = 'We are happy.'
result = Solution().replaceSpace(a)
print(result)
