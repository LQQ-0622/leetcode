class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrace(s, left, right):
            if len(s) == 2 * n:
                result.append(''.join(s))
            if left < n:
                s.append('(')
                backtrace(s, left + 1, right)
                s.pop()
            if right < left:
                s.append(')')
                backtrace(s, left, right + 1)
                s.pop()

        backtrace([], 0, 0)
        return result


result = Solution().generateParenthesis(4)
print(result)
